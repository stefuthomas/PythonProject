etunimi = input('Anna "etunimesi": ')
syntymävuosi = int(input("Anna syntymävuotesi: "))

ikä = 2023-syntymävuosi


jakojäännös = ikä%10
jäljellä=10-jakojäännös
pyöreitä_juhlittu = ikä//10

print(f"Hienoa, {etunimi}! juhlit pyöreitä vuosia {jäljellä} vuoden päästä. Täytät silloin{(pyöreitä_juhlittu+1)*10} ")