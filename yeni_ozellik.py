#!/usr/bin/env python3
"""
Yeni Özellik Modülü
--------------------
Bu modül, mcp-test-repo için yeni özellikler içerir.
"""

class YeniOzellik:
    """Yeni özellikleri temsil eden sınıf."""
    
    def __init__(self, isim="Varsayılan"):
        """
        Yeni özellik için yapılandırıcı.
        
        Args:
            isim (str): Özelliğin ismi
        """
        self.isim = isim
        self.aktif = False
    
    def etkinlestir(self):
        """Özelliği etkinleştirir."""
        self.aktif = True
        print(f"{self.isim} özelliği etkinleştirildi!")
        return True
    
    def devredisi_birak(self):
        """Özelliği devre dışı bırakır."""
        self.aktif = False
        print(f"{self.isim} özelliği devre dışı bırakıldı!")
        return True
    
    def durum_raporu(self):
        """
        Özelliğin durumunu döndürür.
        
        Returns:
            dict: Özelliğin durumunu içeren sözlük
        """
        return {
            "isim": self.isim,
            "durum": "etkin" if self.aktif else "devre dışı"
        }


def ornek_kullanim():
    """Örnek kullanım fonksiyonu."""
    ozellik = YeniOzellik("Test Özelliği")
    ozellik.etkinlestir()
    print(ozellik.durum_raporu())
    ozellik.devredisi_birak()
    print(ozellik.durum_raporu())


if __name__ == "__main__":
    ornek_kullanim()
