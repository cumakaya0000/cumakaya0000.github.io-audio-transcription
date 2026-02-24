from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu")

segments, info = model.transcribe(
    r"C:\Users\kcuma\Desktop\dersler\tarih\ses.wav",
    language="tr",
    vad_filter=True
)

with open("cikti.txt", "w", encoding="utf-8") as f:
    for s in segments:
        satir = f"[{s.start:.1f}-{s.end:.1f}] {s.text}\n"
        print(satir, end="")
        f.write(satir)

print("\nBitti. cikti.txt oluşturuldu.")