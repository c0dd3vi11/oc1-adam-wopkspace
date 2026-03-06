#!/usr/bin/env python3
import argparse
import json
import sys
from faster_whisper import WhisperModel


def main() -> int:
    p = argparse.ArgumentParser(description="Transcribe audio with faster-whisper")
    p.add_argument("audio_path")
    p.add_argument("--model", default="small", help="tiny, base, small, medium, large-v3")
    p.add_argument("--beam-size", type=int, default=5)
    p.add_argument("--language", default=None, help="Optional language code, e.g. ru/en")
    p.add_argument("--json", action="store_true", help="Print JSON output")
    args = p.parse_args()

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(args.audio_path, beam_size=args.beam_size, language=args.language)

    segs = []
    text_parts = []
    for s in segments:
        txt = (s.text or "").strip()
        if not txt:
            continue
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": txt})
        text_parts.append(txt)

    full_text = " ".join(text_parts).strip()
    payload = {
        "language": info.language,
        "language_probability": float(info.language_probability or 0.0),
        "text": full_text,
        "segments": segs,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(full_text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
