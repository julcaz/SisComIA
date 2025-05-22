def diagnosticar():
    print("Sistema Experto: Diagnóstico de fallas comunes en computadoras\n")
    
    cable_conectado = input("¿El cable de alimentación está conectado? (s/n): ").lower() == "s"
    enciende = input("¿La computadora enciende? (s/n): ").lower() == "s"
    pantalla_azul = input("¿Aparece una pantalla azul? (s/n): ").lower() == "s"
    arranca_sistema = input("¿El sistema operativo carga correctamente? (s/n): ").lower() == "s"
    ventilador_suena = input("¿El ventilador suena mucho? (s/n): ").lower() == "s"
    se_apaga = input("¿La computadora se apaga sola? (s/n): ").lower() == "s"
    pitidos = input("¿La computadora emite pitidos al encender? (s/n): ").lower() == "s"
    lento = input("¿La computadora está muy lenta? (s/n): ").lower() == "s"
    se_reinicia = input("¿La computadora se reinicia sola? (s/n): ").lower() == "s"
    detecta_disco = input("¿Detecta el disco duro en la BIOS? (s/n): ").lower() == "s"

    print("\nPosibles causas:")

   
    if not enciende and not cable_conectado:
        print("- Verifica que el cable de alimentación esté bien conectado.")
    if not enciende and cable_conectado:
        print("- Revisa la fuente de poder.")
    if pantalla_azul:
        print("- Puede haber un problema con la memoria RAM o los drivers.")
    if enciende and not arranca_sistema:
        print("- Revisa el disco duro o el sistema operativo.")
    if ventilador_suena and se_apaga:
        print("- Posible sobrecalentamiento, limpia el ventilador.")
    if pitidos:
        print("- Diagnóstico por pitidos: puede indicar fallas de hardware como RAM o tarjeta madre.")
    if enciende and se_apaga:
        print("- Revisa la fuente de poder o la tarjeta madre.")
    if lento:
        print("- Verifica el uso de CPU y memoria RAM.")
    if se_reinicia:
        print("- Puede ser un problema de sobrecalentamiento o fuente de poder defectuosa.")
    if not detecta_disco:
        print("- Revisa la conexión del disco duro o la configuración en la BIOS.")

    print("\nDiagnóstico terminado.")


diagnosticar()
