use ruff_db::files::File;
use ruff_db::parsed::parsed_module;
use ruff_python_ast::name::Name;
use ruff_python_ast::{self as ast, Stmt};
use ruff_text_size::{Ranged, TextRange};

use crate::Db;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct WorkspaceSymbolInfo {
    pub name: Name,
    pub kind: SymbolKind,
    pub file: File,
    pub name_range: TextRange,
    pub full_range: TextRange,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SymbolKind {
    Module,
    Class,
    Function,
    Method,
    Variable,
    Constant,
    Parameter,
    Import,
}

pub fn all_symbols(db: &dyn Db, file: File) -> Vec<WorkspaceSymbolInfo> {
    let parsed = parsed_module(db.upcast(), file).load(db.upcast());
    let mut symbols = Vec::new();
    collect_symbols(&parsed.syntax().body, file, &mut symbols);
    symbols
}

fn collect_symbols(stmts: &[Stmt], file: File, symbols: &mut Vec<WorkspaceSymbolInfo>) {
    for stmt in stmts {
        match stmt {
            Stmt::ImportFrom(import_from) => {
                for alias in &import_from.names {
                    let name_range = if alias.name.as_str() == "*" {
                        import_from
                            .module
                            .as_ref()
                            .map(|m| m.range())
                            .unwrap_or(alias.range())
                    } else {
                        alias.range()
                    };
                    symbols.push(WorkspaceSymbolInfo {
                        name: Name::new(alias.name.as_str()),
                        kind: SymbolKind::Import,
                        file,
                        name_range,
                        full_range: alias.range(),
                    });
                }
            }
            _ => {}
        }
    }
}
