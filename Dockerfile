FROM --platform=$BUILDPLATFORM ubuntu AS build
ENV HOME="/root"
WORKDIR $HOME

RUN apt update && apt install -y build-essential curl python3-venv

# Setup zig as cross compiling linker
RUN python3 -m venv $HOME/.venv
RUN .venv/bin/pip install cargo-zigbuild
ENV PATH="$HOME/.venv/bin:$PATH"

# Change to the ruff directory, which is the root for our build
WORKDIR $HOME/ruff

# Install rust
ARG TARGETPLATFORM
RUN case "$TARGETPLATFORM" in \
    "linux/arm64") echo "aarch64-unknown-linux-musl" > rust_target.txt ;; \
    "linux/amd64") echo "x86_64-unknown-linux-musl" > rust_target.txt ;; \
    *) exit 1 ;; \
    esac
# Update rustup whenever we bump the rust version
COPY ruff/rust-toolchain.toml rust-toolchain.toml
ARG BUILDARCH
ARG RUSTUP_VERSION=1.28.2
RUN case "$BUILDARCH" in \
        "amd64") rustup_target="x86_64-unknown-linux-gnu"; rustup_sha256="20a06e644b0d9bd2fbdbfd52d42540bdde820ea7df86e92e533c073da0cdd43c" ;; \
        "arm64") rustup_target="aarch64-unknown-linux-gnu"; rustup_sha256="e3853c5a252fca15252d07cb23a1bdd9377a8c6f3efa01531109281ae47f841c" ;; \
        *) exit 1 ;; \
    esac && \
    curl --proto '=https' --tlsv1.2 -sSf "https://static.rust-lang.org/rustup/archive/${RUSTUP_VERSION}/${rustup_target}/rustup-init" -o /tmp/rustup-init && \
    echo "${rustup_sha256}  /tmp/rustup-init" | sha256sum -c - && \
    chmod +x /tmp/rustup-init && \
    /tmp/rustup-init -y --target "$(cat rust_target.txt)" --profile minimal --default-toolchain none && \
    rm /tmp/rustup-init
ENV PATH="$HOME/.cargo/bin:$PATH"
# Installs the correct toolchain version from rust-toolchain.toml and then the musl target
RUN rustup target add $(cat rust_target.txt)

# Build
COPY ruff/crates crates
COPY ruff/Cargo.toml Cargo.toml
COPY ruff/Cargo.lock Cargo.lock
COPY dist-workspace.toml ../dist-workspace.toml
RUN cargo zigbuild --bin ty --target $(cat rust_target.txt) --release
RUN cp target/$(cat rust_target.txt)/release/ty /ty
# TODO: Optimize binary size, with a version that also works when cross compiling
# RUN strip --strip-all /ty

FROM scratch
COPY --from=build /ty /ty
WORKDIR /io
ENTRYPOINT ["/ty"]
