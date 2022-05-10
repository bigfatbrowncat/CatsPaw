import fontforge as ff
import psMat

name = "CatsPaw"

cpf = ff.open(f"{name}-Base.sfd")

# Thin

for sym in cpf.selection.all():
    cpf[sym].removeOverlap()
    cpf[sym].correctDirection()
    cpf[sym].stroke("elliptical", 1, 30, -5, removeinternal=True) #flags=('cleanup'))
    cpf[sym].changeWeight(5)


weight = "Thin"
cpf.weight = weight
cpf.fontname = f"{name}-{weight}"
cpf.fullname = f"{name} {weight}"

cpf.save(f"{name}-{weight}.sfd")


# Regular (from Thin)

for sym in cpf.selection.all():
    cpf[sym].removeOverlap()
    cpf[sym].correctDirection()
    cpf[sym].stroke("elliptical", 1, 10, -5, removeinternal=True) #flags=('cleanup'))
    cpf[sym].changeWeight(10)

weight = "Regular"
cpf.weight = weight
cpf.fontname = f"{name}-{weight}"
cpf.fullname = f"{name} {weight}"

cpf.save(f"{name}-{weight}.sfd")


# Bold (from Regular)

#SCALE_MATRIX = psMat.scale(1.1, 1.0)

for sym in cpf.selection.all():
    cpf[sym].removeOverlap()
    cpf[sym].correctDirection()
    #cpf[sym].transform(SCALE_MATRIX)
    cpf[sym].condenseExtend(1.1, 10)
    cpf[sym].changeWeight(20)
    

weight = "Bold"
cpf.weight = weight
cpf.fontname = f"{name}-{weight}"
cpf.fullname = f"{name} {weight}"

cpf.save(f"{name}-{weight}.sfd")
