from PIL import Image

types = ['boxplot','CA']
contents = ['cq','fmax','mean pcr','melt range','melt start','melt stop','pcr min','pcr start','pcr stop','reverse cq']
channels = [415,445,480,515,555,590,630,680,'NIR','CLR','DARK']


def findPlot(type,content,channel):
    im = ''.join(['plotsCovid/',str(channel),'_',content,'_',type,'.png'])
    image = Image.open(im)
    image.show()


findPlot('boxplot','reverse cq','515')
# for i in contents:
#     # findPlot('boxplot',i,480)
#     findPlot('CA','melt stop','515')