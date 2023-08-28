sukupuoliN = "nainen"
sukupuoliM = "mies"

sukupuoli = (input("Anna sukupuolesi: "))
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvosi (g/l): "))


if sukupuoli == sukupuoliN and 117<=hemoglobiiniarvo<=175:
    print("hemoglobiiniarvosi on normaali naiselle.")
elif sukupuoli == sukupuoliN and 117>=hemoglobiiniarvo:
    print("hemoglobiiniarvosi on alhainen naiselle.")
elif sukupuoli == sukupuoliN and 175<=hemoglobiiniarvo:
    print("hemoglobiiniarvosi on korkea naiselle.")
if sukupuoli == sukupuoliM and 134<=hemoglobiiniarvo<=195:
    print("hemoglobiiniarvosi on normaali miehelle.")
elif sukupuoli == sukupuoliM and 134>=hemoglobiiniarvo:
    print("hemoglobiiniarvosi on alhainen miehelle.")
elif sukupuoli == sukupuoliM and 195<=hemoglobiiniarvo:
    print("hemoglobiimiarvosi on korkea miehelle.")