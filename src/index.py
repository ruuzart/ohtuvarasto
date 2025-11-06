from varasto import Varasto
#muutos
def tulosta_alkutilanne(mehu_varasto, olut_varasto):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu_varasto}")
    print(f"Olutvarasto: {olut_varasto}")

def tulosta_olut_getterit(varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def kasittele_mehu_operaatiot(varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto}")

def nayta_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def kasittele_olut_virhetilanteet(varasto):
    print(f"Olutvarasto: {varasto}")
    print("olutta.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {varasto}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {varasto}")

def kasittele_mehu_virhetilanteet(varasto):
    print(f"Mehuvarasto: {varasto}")
    print("mehua.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {varasto}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {varasto}")

def main():
    mehu = Varasto(100.0)
    olut = Varasto(100.0, 20.2)

    tulosta_alkutilanne(mehu, olut)
    tulosta_olut_getterit(olut)
    kasittele_mehu_operaatiot(mehu)
    nayta_virhetilanteet()
    kasittele_olut_virhetilanteet(olut)
    kasittele_mehu_virhetilanteet(mehu)

if __name__ == "__main__":
    main()
