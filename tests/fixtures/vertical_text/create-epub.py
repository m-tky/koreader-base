#!/usr/bin/env python3
"""
Create a minimal Japanese EPUB for vertical text testing.
This EPUB contains simple Japanese text without ruby annotations (for Phase 1).
"""

import zipfile
import os
import sys

EPUB_CONTENT = {
    "mimetype": "application/epub+zip",
    "META-INF/container.xml": """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
""",
    "content.opf": """<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="uid">vertical-text-test</dc:identifier>
    <dc:title>Vertical Text Test</dc:title>
    <dc:language>ja</dc:language>
    <meta property="dcm:textDirection">vertical-rl</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="chapter1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>
    <item id="style" href="style.css" media-type="text/css"/>
  </manifest>
  <spine>
    <itemref idref="chapter1"/>
  </spine>
</package>
""",
    "nav.xhtml": """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>Navigation</title>
</head>
<body>
  <nav epub:type="toc">
    <h1>Table of Contents</h1>
    <ol>
      <li><a href="chapter1.xhtml">Chapter 1</a></li>
    </ol>
  </nav>
</body>
</html>
""",
    "chapter1.xhtml": """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Chapter 1</title>
  <meta charset="UTF-8"/>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <section>
    <h1>第一章</h1>
    <p>これは縦書きのテスト用テキストです。日本語の小説では通常、文字は上から下へ、そして右から左へと流れます。縦書きの文章は、古来より日本の書物において使われてきた伝統的な書き方です。</p>
    <p>吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。</p>
    <p>私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚かる遠慮というよりも、その方が私にとって自然だからである。先生の家はいつも静かであった。</p>
    <p>枕草紙は、清少納言によって書かれた日本最古の随筆の一つです。春はあけぼの。やうやう白くなりゆく山際、少し明りて、紫だちたる雲の細くたなびきたる。夏は夜。月の頃はさらなり。闇もなほ、蛍の多く飛びちがひたる。</p>
    <p>方丈記は、鴨長明によって書かれた隠士文学の代表作です。行く川の流れは絶えずして、しかももとの水にあらず。よどみに浮かぶうたかたは、かつ消えかつ結びて、久しくとどまりたる例なし。世の中にある人とすみかと、またかくのごとし。</p>
    <p>源氏物語は、紫式部によって書かれた日本最古の長編小説です。いづれの御時にか、女御、更衣、あまたさふらひたまひけるなかに、いとやむごとなき際にはあらぬが、すぐれて時めきたまふありけり。はじめより我はと思ひあがりたまへる御方々、めざましきものにおとしめそねみたまふ。</p>
    <p>平家物語は、鎌倉時代から室町時代にかけて成立した軍記物語です。祇園精舎の鐘の声、諸行無常の響きあり。沙羅双樹の花の色、盛者必衰の理をあらはす。おごれる人も久しからず、ただ春の夜の夢のごとし。猛き者もつひには滅びぬ、ひとへに風の前の塵に同じ。</p>
    <p>徒然草は、吉田兼好によって書かれた随筆です。つれづれなるままに、日暮しがた、硯にむかひて、心にうつりゆくよしなしごとを、そこはかとなく書き付くべし。怪しうこそものぐるほしけれ。世は定めなきこそ、いみじけれ。</p>
    <p>伊勢物語は、平安時代中期に成立した歌物語です。むかしおとこありけり。小冠たてて、上襲の色は濃き青に、下襲は襲の色にして、筋弓はり、靫に矢をゐれて、狩をしけり。その男、しのぶずりの狩衣をなむ着たりける。</p>
    <p>竹取物語は、日本最古の物語文学です。いまは昔、竹取の翁といふものありけり。その翁、竹とりをすること数年になりけり。その竹の中に、光る竹一筋ありけり。あやしがりて寄りて見るに、筒の中光りたり。それを見れば、三寸ばかりなる人、いとうつくしうてゐたり。</p>
    <p>万葉集は、奈良時代末期に成立した日本最古の和歌集です。天地の分かれし時ゆ、神さびて高く貴き駿河なる富士の高嶺を天の原ふりさけ見れば、渡る日の影も隠らひ、照る月の光も見えず、白雲もい行きはばかり、時じくそ雪は降りける。語り継ぎ言い継ぎゆかむ不尽の高嶺は。</p>
    <p>古今和歌集は、平安時代初期に撰進された勅撰和歌集です。やまとうたは、人の心を種として、よろづの言の葉とぞなれりける。世の中にある人、ことわざしげきものなれば、心に思ふことを、見るもの聞くものにつけて、言ひいだせるなり。花に鳴くうぐひす、水にすむかはづの声を聞けば、生きとし生けるもの、いづれか歌をよまざりける。</p>
  </section>
</body>
</html>
""",
    "style.css": """body {
  writing-mode: vertical-rl;
  margin: 0;
  padding: 0;
  font-family: serif;
  font-size: 14pt;
  line-height: 1.8;
}
h1 {
  font-size: 1.2em;
  text-align: center;
  margin: 0.5em;
}
p {
  text-indent: 1em;
  margin: 0.3em 0;
}
"""
}

def create_epub(output_path):
    """Create a minimal EPUB file."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # mimetype must be first and uncompressed
        zf.writestr("mimetype", EPUB_CONTENT["mimetype"], compress_type=zipfile.ZIP_STORED)
        for name, content in EPUB_CONTENT.items():
            if name != "mimetype":
                zf.writestr(name, content.encode('utf-8'))
    print(f"Created: {output_path}")

if __name__ == "__main__":
    output = sys.argv[1] if len(sys.argv) > 1 else "simple_ja_noruby.epub"
    create_epub(output)
