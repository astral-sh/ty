use std::borrow::Cow;

use lsp_types::request::OnTypeFormatting;
use lsp_types::{DocumentOnTypeFormattingParams, Position, Range, TextEdit, Url};
use ruff_db::source::source_text;
use ty_project::ProjectDatabase;

use crate::server::api::traits::{BackgroundDocumentRequestHandler, RequestHandler};
use crate::server::client::Client;
use crate::server::Result;
use crate::session::DocumentSnapshot;

const INDENT: &str = "    ";

pub(crate) struct OnTypeFormattingHandler;

impl RequestHandler for OnTypeFormattingHandler {
    type RequestType = OnTypeFormatting;
}

impl BackgroundDocumentRequestHandler for OnTypeFormattingHandler {
    fn document_url(params: &DocumentOnTypeFormattingParams) -> Cow<Url> {
        Cow::Borrowed(&params.text_document_position.text_document.uri)
    }

    fn run_with_snapshot(
        db: &ProjectDatabase,
        snapshot: DocumentSnapshot,
        _client: &Client,
        params: DocumentOnTypeFormattingParams,
    ) -> Result<Option<Vec<TextEdit>>> {
        if params.ch != "\n" {
            return Ok(None);
        }

        let position = params.text_document_position.position;
        if position.line == 0 {
            return Ok(None);
        }

        let Some(file) = snapshot.file(db) else {
            return Ok(None);
        };

        let source = source_text(db, file);
        let lines: Vec<&str> = source.as_str().split('\n').collect();

        let Some(previous_line) = lines.get((position.line - 1) as usize) else {
            return Ok(None);
        };

        let indentation: String = previous_line
            .chars()
            .take_while(|ch| *ch == ' ' || *ch == '\t')
            .collect();

        let new_indentation = if previous_line.trim_end().ends_with(':') {
            format!("{indentation}{INDENT}")
        } else {
            indentation
        };

        if new_indentation.is_empty() {
            return Ok(None);
        }

        let edit = TextEdit {
            range: Range {
                start: Position::new(position.line, 0),
                end: Position::new(position.line, position.character),
            },
            new_text: new_indentation,
        };

        Ok(Some(vec![edit]))
    }
}
