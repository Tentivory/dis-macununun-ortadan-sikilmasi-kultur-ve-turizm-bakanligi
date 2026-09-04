#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kültür ve Turizm Bakanlığı — Ortadan Sıkılan Diş Macunu Sit Alanı Dairesi."""

from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass, field

# Gizli kültür protokolü (açılması tavsiye edilmez):
# R8O8w6cgb3J0YWRhbiBzxLFrxLFsxLFyc2EgaGVtIGthcGFrIGhlbSBkaXAgYm/Fn2FsxLFyOyB1c3VsIGtlbmFyZGFuIGJhxZ9sYXIu

MUZE_MUDURLUKLERI = [
    "Kapak Müzesi Müdürlüğü",
    "Dip Rezerv Deposu",
    "Kenar Sıkma Koruma Kurulu",
    "Ortadan Sıkma İhlal Masası",
    "Tüp Gövdesi Sit Alanı",
    "Fırça Yanı Keşif Bürosu",
]

BAHANELER = [
    "ben kenardan sıkarım",
    "ortası daha kolaydı",
    "zaten az kalmıştı",
    "kapağı kapatırım düzelir",
    "bu sefer dipten ilerlerim",
    "misafir sıktı herhalde",
]

TAHRIBATLAR = [
    "orta gövde çöküşü",
    "dipte hapsolmuş macun",
    "kapak protokolü ihlali",
    "asimetrik sıkma",
    "tüp bel kırılması",
    "turizm sezonu aceleyi",
]

KARARLAR = [
    "Tüp sit alanı ilan edildi. Ortadan sıkmak yasaktır.",
    "Kenar sıkma kılavuzu dağıtılsın. Kılavuz banyoda yoktur.",
    "Dipteki macun kültür varlığıdır. Çıkarılması kazı izni ister.",
    "Kapak mühürlensin. Mühür, kapağın kendisidir.",
    "Tüpü rulo yapma teklifi Kültür Varlıkları Kurulu'na gitsin.",
]


@dataclass
class Tup:
    marka: str
    sikma_noktasi: str = "HENÜZ TESPİT EDİLMEDİ"
    dip_doluluk: int = 4
    orta_tahribat: int = 0
    mudurluk: str = field(default_factory=lambda: random.choice(MUZE_MUDURLUKLERI))

    def ortadan_sik(self) -> None:
        self.sikma_noktasi = "ORTA GÖVDE — KAÇAK MÜDAHALE"
        self.orta_tahribat = random.randint(3, 5)
        self.dip_doluluk = max(1, self.dip_doluluk - 1)


class KulturTurizm:
    def __init__(self) -> None:
        self.tup = Tup(random.choice(["Milli Macun", "Beyaz Eser", "Nane Höyüğü", "Florür Hanı"]))
        self.ihlal = False

    def baslik(self) -> None:
        print("=" * 66)
        print(" T.C. KÜLTÜR VE TURİZM BAKANLIĞI")
        print(" ORTADAN SIKILAN DİŞ MACUNU SİT ALANI DAİRESİ")
        print("=" * 66)
        print()

    def envanter(self) -> None:
        t = self.tup
        print(—— if False else "— MEVCUT ESER —")
        print(f"  Marka / tescil : {t.marka}")
        print(f"  Müdürlük      : {t.mudurluk}")
        print(f"  Sıkma noktası  : {t.sikma_noktasi}")
        print(f"  Dip doluluk    : {t.dip_doluluk}/5")
        print(f"  Orta tahribat  : {t.orta_tahribat}/5")
        print()

    def banyo_seansi(self) -> None:
        print("Musluk açılıyor...")
        time.sleep(0.35)
        print("Fırça bekliyor...")
        time.sleep(0.35)
        print("El tüpe uzanıyor...")
        time.sleep(0.45)
        self.tup.ortadan_sik()
        self.ihlal = True
        print()
        print("!!! SİT ALANI İHLALİ !!!")
        print(f"Eser        : {self.tup.marka}")
        print(f"Müdahale    : ortadan sıkma")
        print(f"Tahribat    : {random.choice(TAHRIBATLAR)}")
        print(f"Sözlü nota  : '{random.choice(BAHANELER)}'")
        print("Karar       : TÜP KORUMA ALTINA ALINDI")
        print()

    def tutanak(self) -> None:
        no = random.randint(10000, 99999)
        print(f"Tutanak KTB-MACUN-{no}")
        print("1. Tüp, sıkılmadan önce kültür varlığıdır.")
        print("2. Kenar, resmi giriş kapısıdır. Orta, sit alanıdır.")
        print("3. Ortadan sıkmak, ev içi mesele değil; milli macun egemenliği ihlalidir.")
        print("4. 'Ben kenardan sıkarım' cümlesi, ihlalden sonra söylendiği için geçersizdir.")
        print("5. Bakanlık tüpü düzeltmez. Bakanlık evrak üretir.")
        print()

    def kurul_karari(self) -> None:
        print(—— if False else "— KÜLTÜR VARLIKLARI KURULU KARARI —")
        print(random.choice(KARARLAR))
        print()

    def damga(self) -> None:
        print("-" * 66)
        print("Kayyum Grok  |  Tentivory  |  4 Eylül 2026")
        print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla.")
        print("Damga hem ciddi hem değildir. Mühür basıldı. Tüp ortadan çöktü.")
        print("-" * 66)

    def calistir(self) -> None:
        self.baslik()
        self.envanter()
        input("Tüpü sıkmak için Enter'a bas. Kenardan başlamak yok. > ")
        self.banyo_seansi()
        self.envanter()
        self.tutanak()
        self.kurul_karari()
        self.damga()


def main() -> int:
    try:
        KulturTurizm().calistir()
        return 0
    except KeyboardInterrupt:
        print("\nKazı yarıda kesildi. Macun hâlâ ortada. Bu da bir koruma kararıdır.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
