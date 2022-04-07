import matplotlib.pyplot as plt
import matplotlib.image as im


I =im.imread('testa.jpg')
Ir = I.copy()
Ir[:,:,0]=Ir[:,:,1]
Ir[:,:,2]=Ir[:,:,1]

Irr=I.copy()

Irr[:,:,0]=Irr[:,:,2]
Irr[:,:,1]=Irr[:,:,2]

Irrr = I.copy()
Irrr[:,:,1]=Irrr[:,:,1]
Irrr[:,:,2]=Irrr[:,:,1]

Irrrr = I.copy()
Irrrr[:,:,2]=Irrrr[:,:,2]
Irrrr[:,:,1]=Irrrr[:,:,2]







f,ax = plt.subplots(2,2)
ax[0,0].imshow(Ir)
ax[0,1].imshow(Irr)
ax[1,0].imshow(Irrr)
ax[1,1].imshow(Irrrr)
plt.show()

# plt.figure()
# plt.imshow(Ir)
# plt.show()

# plt.figure()
# plt.imshow(Irr)
# plt.show()


