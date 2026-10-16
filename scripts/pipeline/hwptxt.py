"""HWP(5.x) 본문 텍스트를 문단 단위로 추출. 사용: python3 -I hwptxt.py file.hwp"""
import sys, zlib, struct, olefile

def paragraphs(path):
    ole = olefile.OleFileIO(path)
    hdr = ole.openstream("FileHeader").read()
    compressed = bool(struct.unpack_from("<I", hdr, 36)[0] & 1)
    secs = sorted([e for e in ole.listdir() if e[0] == "BodyText"], key=lambda e: int(e[1][7:]))
    for e in secs:
        data = ole.openstream(e).read()
        if compressed:
            data = zlib.decompress(data, -15)
        i = 0
        while i < len(data):
            h = struct.unpack_from("<I", data, i)[0]; i += 4
            tag, size = h & 0x3FF, (h >> 20) & 0xFFF
            if size == 0xFFF:
                size = struct.unpack_from("<I", data, i)[0]; i += 4
            if tag == 67:
                yield decode(data[i:i + size])
            i += size

def decode(b):
    out, j = [], 0
    while j + 1 < len(b):
        c = struct.unpack_from("<H", b, j)[0]
        if c < 32:
            if c in (9,):
                out.append("\t"); j += 2
            elif c in (10, 13):
                j += 2
            elif c in (0, 24, 25, 26, 27, 28, 29, 30, 31):
                j += 2
            else:
                j += 16  # 확장/인라인 컨트롤은 8글자(16바이트)
            continue
        out.append(chr(c)); j += 2
    return "".join(out).strip()

if __name__ == "__main__":
    for p in paragraphs(sys.argv[1]):
        if p:
            print(p)
