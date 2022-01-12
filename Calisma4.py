a = (9589,358,247,'python',27)

b = (1,2,5,'python',10)
print("python"[0])
print(a)
print(len(a))
oyuncu = ["Arda","Turazan",31,1.89]
print(oyuncu)
print(oyuncu[1])
oyuncu[1] = "yilmaz"
print(oyuncu[1])
print(oyuncu)
oyuncu[2] = "69"
print(oyuncu)
oyuncu[0] = "Riaz"
print(oyuncu)
oyuncu[3] = "2.16"
print(oyuncu)
print("***** 1- To add a new element to the list. ****")
oyuncu.append("Galatasaray")
print(oyuncu)
print("python" + "calismasi")
print("***** 2- To add a new element to the list. ****")
oyuncu = oyuncu + ["Juventus"]
print(oyuncu)
print("yazilim"[:2])

print("*****Print the list's elements until the given index****")
print(oyuncu[:2])

print("*****To change the list's elements until the given index****")
oyuncu[:2] = ["cristiano","ronaldo"]
print("*****To make empty for the list's elements until the given index****")
oyuncu[:2] = []
print(oyuncu)
oyuncu[:] = []
print(oyuncu)


