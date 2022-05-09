import fontforge as ff

name = "CatsPaw"

cpf = ff.open(f"{name}-Base.sfd")

for sym in cpf.selection.all():
    cpf[sym].removeOverlap()
    cpf[sym].correctDirection()
    cpf[sym].stroke("elliptical", 1, 30, -5, removeinternal=True) #flags=('cleanup'))
    cpf[sym].changeWeight(15)


weight = "Thin"
cpf.weight = weight
cpf.fontname = f"{name}-{weight}"
cpf.fullname = f"{name} {weight}"

cpf.save(f"{name}-{weight}.sfd")
