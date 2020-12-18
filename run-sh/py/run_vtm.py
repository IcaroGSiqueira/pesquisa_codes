import os

f = 32 # numero de frames

qps = [22,27,32,37]

#confs = ["encoder_randomaccess_vtm.cfg","encoder_lowdelay_vtm.cfg","encoder_intra_vtm.cfg"]

confs = ["encoder_randomaccess_vtm.cfg"]
confs_sigla = ["RA","LD","IO"]

minqs = [8,16,32]
minqsatv = 0 # usar minqs = 1

OPT = 0 # optimizacoes ligadas = 1

gprof = 0 # profilling ligado = 1

taps = 8 # padrão 8

threads = 4 # numero de processos em parelelo

#yuvs=["Campfire_3840x2160_30fps_10bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv"]#ClasseA1

#yuvs=["ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]#ClasseA2

#yuvs=["BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv"]#ClasseB

#yuvs=["RaceHorses_832x480_30fps_8bit_420","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"]#ClasseC

#yuvs=["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30fps_8bit_420.yuv"]#ClasseD

#yuvs=["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv"]#ClasseE

#yuvs=[ArenaOfValor_1920x1080_60fps_8bit_420.yuv,"BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30.yuv"]#ClasseF


#yuvsvvc = ["MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","ArenaOfValor_1920x1080_60fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]#,"CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv"]	#VVC

#yuvshevc = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"]	#VVC_HEVC

yuvs = ["Cactus_1920x1080_50.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv"]

#server ufrgs video paths
yuvh = "/videos"
yuvr = "/home/grellert/yuvs_vtm"

outpath = "/home/grellert/output_VTM"
outpath = "/home/icaro/output_VTM"

encpath = "/home/grellert/vtm10.1"
encpath = "/home/icaro/vvc_10.0"

confpath = "%s/cfg"%encpath
binpath = "%s/bin"%encpath

shpath = "../vtm"

filename = "run_vtm.sh"

#yuvs = os.listdir("/home/icaro/origCfP")

file = open("%s/%s"%(shpath,filename),"w")

try:
	os.system("mkdir ../vtm")
except:
	pass

try:
	os.system("mkdir %s/"%(outpath))
except:
	pass

try:
	os.system("mkdir %s/bin"%(outpath))
except:
	pass

try:
	os.system("mkdir %s/out"%(outpath))
except:
	pass

if gprof == 1:
	try:
		os.system("mkdir %s/gprof"%(outpath))
	except:
		pass

	try:
		os.system("mkdir %s/gmon"%(outpath))
	except:
		pass

inf = ""

if taps == 8:
	taps = ""
else:
	taps = "--fme_filter_ntaps=%s"%taps
	inf = inf + "_" + "taps"

if OPT == 1:
	simd = "AVX2"
	inf = inf + "_" + "OPT"
else:
	simd = "SCALAR"
	inf = inf + "_" + "noOPT"

if gprof == 0:
	#bina = "EncoderAppStatic_std"
	bina = "EncoderAppStatic"
else:
	#bina = "EncoderAppStaticd_std"
	bina = "EncoderAppStaticd"
	inf = inf + "_" + "gprof"

minqsC = 0
if minqsatv == 1:
	minqsC = len(minqs)

conf_n = 0
for conf in confs:
	for yuv in yuvs:
		for qp in qps:
			for minq in range(minqsC):

				print(yuv)
				try:
					vid,pix,fr,b,dummy = yuv.split("_")
					b = b.strip("bit")
					fr = fr.strip("fps")
					nome = vid+"_"+pix+"_"+fr+"fps_"+b+"bit"

				except:
					try:
						vid,pix,fr = yuv.split("_")
						fr = fr.strip(".yuv")

						nome = vid+"_"+pix+"_"+fr+"fps_"

					except:
						vid = yuv.split("_")[0]
						pix = yuv.split("_")[1]

						nome = vid+"_"+pix+"_"

					w,h = pix.split("x")

					if w*h < 8294400:
						b = "8"
					else:
						b = "10"

					nome = nome+b+"bit"

				inf = "%sqp_%sframes_%s_"%(qp,f,confs_sigla[conf_n]) + inf


				#linha = "%s/%s/%s -c %s/%s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --MinQTLumaISlice=%s --MinQTChromaISliceInChromaSamples=%s --MinQTNonISlice=%s --InputBitDepth=%s --SIMD=%s -b \"%s/%s/bin/%s_%s.bin\" "%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,minq,int(minq/2),minq,b,simd,homepath,outpath,nome,info) # Linha de configuracao da codificacao

				if yuv in ["MarketPlace_1920x1080_60fps_10bit_420.yuv",
					"RitualDance_1920x1080_60fps_10bit_420.yuv",
					"ArenaOfValor_1920x1080_60fps_8bit_420.yuv",
					"BasketballDrillText_832x480_50fps_8bit_420.yuv",
					"SlideShow_1280x720_20fps_8bit_420.yuv",
					"Campfire_3840x2160_30fps_10bit_420.yuv",
					"KristenAndSara_1280x720_60fps_8bit_420.yuv",
					"FoodMarket4_3840x2160_60fps_10bit_420.yuv",
					"Tango2_3840x2160_60fps_10bit_420.yuv",
					"ParkRunning3_3840x2160_50fps_10bit_420.yuv",
					"CatRobot_3840x2160_60fps_10bit_420.yuv",
					"DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]:

					linha = "%s/%s -c %s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --InputBitDepth=%s %s --SIMD=%s -b \"%s/bin/%s_%s.bin\" "%(binpath,bina,confpath,conf,yuvh,yuv,fr,w,h,qp,f,b,taps,simd,outpath,nome,info) # Linha de configuracao da codificacao

				elif yuv in ["RaceHorses_832x480_30.yuv",
					"BasketballDrill_832x480_50.yuv",
					"BQMall_832x480_60.yuv",
					"PartyScene_832x480_50.yuv",
					"BlowingBubbles_416x240_50.yuv",
					"BQSquare_416x240_60.yuv",
					"BasketballPass_416x240_50.yuv",
					"RaceHorses_416x240_30.yuv",
					"BasketballDrive_1920x1080_50.yuv",
					"BQTerrace_1920x1080_60.yuv",
					"Cactus_1920x1080_50.yuv",
					"FourPeople_1280x720_60.yuv",
					"Johnny_1280x720_60.yuv",
					"SlideEditing_1280x720_30.yuv"]:

					linha = "%s/%s -c %s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --InputBitDepth=%s %s --SIMD=%s -b \"%s/bin/%s_%s.bin\" "%(binpath,bina,confpath,conf,yuvr,yuv,fr,w,h,qp,f,b,taps,simd,outpath,nome,info) # Linha de configuracao da codificacao

				linha1 = "> %s/out/%s_%s.txt"%(outpath,nome,info) # linha da saida da codificacao

				# linhas do profiling
				linha2 = "mv gmon.out %s/gmon/gmon_%s_%s.out"%(outpath,nome,info)

				linha3 = "gprof %s/%s %s/gmon/gmon_%s_%s.out > %s/gprof/%s_%s.txt"%(binpath,bina,outpath,nome,info,outpath,nome,info)

				linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

				if gprof == 1:

					linha1 = "> %s/gprof/out/%s_%s.txt"%(outpath,nome,info) # linha da saida da codificacao

					#VERIFICAR SOBRESCRICAO
					'''
					try:
						test = open("%s/%s"%(shpath,filename),"r")
						tlines = test.readlines()
						tline = tlines[0]
						if linha not in tline:
							file.write(linha + linha1 + " && " + linha4 + "\n")
					except:
						'''
					file.write(linha + linha1 + " && " + linha2 + " && " + linha3 + " && " + linha4 + "\n")

				else:	
					try:
						test = open("%s/%s_%s.txt"%(outpath,nome,info),"r")
						tlines = test.readlines()
						tline = tlines[-1]
						if "Total Time" not in tline:
							file.write(linha + linha1 + " && " + linha4 + "\n")
					except:
						file.write(linha + linha1 + " && " + linha4 + "\n")
	conf_n+=1



i=0
if threads >= 1:

	file = open("%s/%s"%(shpath,filename),"r")

	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)
	nconf = len(confs)

	for x in range(threads):

		try:
			os.system("mkdir %s/script%d"%(shpath,x+1))
		except:
			pass
		file2 = open("%s/script%d/%d_%s.sh"%(shpath,x+1,x+1,inf),"w")
		i = x*nqp
		j=0

		while i < tam:

			line = lines[i]
			file2.write(line)

			i = i+1
			j = j+1

			if j == nqp:
				j=0
				i = (i-nqp)+(nqp*threads)
			# if nqp == 4:
			# 	if ((i-1)%4) == 3:
			# 		i = i+threads*(3)
			# else:
			# 	j = j+1
			# 	div = tam/threads
			# 	if j == div:
			# 		i = i+threads*div
			# 		j=0
		# if gitpull == 1:
		# 	linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
		# 	print >> file2, linhag
	file2.close
file.close
