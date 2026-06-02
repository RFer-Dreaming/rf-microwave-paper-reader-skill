import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Render PDF pages to PNG using PyMuPDF.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--out", required=True, help="Output directory for rendered PNG pages.")
    parser.add_argument("--dpi", type=int, default=300, help="Render DPI. Default: 300.")
    parser.add_argument("--pages", nargs="*", type=int, help="1-based page numbers. Default: all pages.")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        import fitz
    except ModuleNotFoundError as exc:
        raise SystemExit("PyMuPDF is required. Install it with: python -m pip install PyMuPDF") from exc

    pdf_path = Path(args.pdf)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    pages = args.pages or list(range(1, len(doc) + 1))
    matrix = fitz.Matrix(args.dpi / 72.0, args.dpi / 72.0)

    for page_no in pages:
        if page_no < 1 or page_no > len(doc):
            raise ValueError(f"Page {page_no} is outside 1..{len(doc)}")
        pix = doc[page_no - 1].get_pixmap(matrix=matrix, alpha=False)
        out_file = out_dir / f"page_{page_no:02d}_{args.dpi}dpi.png"
        pix.save(out_file)
        print(out_file.resolve())


if __name__ == "__main__":
    main()
