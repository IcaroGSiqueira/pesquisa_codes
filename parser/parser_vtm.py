import os

#OPT = 0 # optimizacoes ligadas = 1

pathin = "./"
out = open("./vtm_br-psnr.csv","w")

yuvs = sorted(os.listdir("%s"%pathin))

linha = "YUV,Y-PSNR,U-PSNR,V-PSNR,YUV-PSNR,BITRATE,TOTAL TIME\n"
#print >> out, linha
out.write(linha)

for yuv in yuvs:
	if ".py" in yuv:
		continue
	if ".bin" in yuv:
		continue
	if ".csv" in yuv:
		continue

	try:
		file = open("%s/%s"%(pathin,yuv),"r")
		lines = file.readlines()
		line = lines[-1]
		dummy,t = line.split(":")
		print(t)
		dummy,t,dummy0 = t.split("]")
		t,dummy = t.split("sec")
		t = t.strip(" ")
		line = lines[-4]
		fl,r = line.split("a")
		r = r.strip(" ")
		br,y,u,v,yuvv = r.split("   ")
		yuvv = yuvv[:-1]
		print(yuv,"DONE! \n")
	except:
		print("\n Saida Incompleta")

	linha = "%s,%s,%s,%s,%s,%s,%s\n"%(yuv,y,u,v,yuvv,br,t)
	out.write(linha)
	out.close
