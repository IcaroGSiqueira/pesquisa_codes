import os

f = 4

#[37,32,27,22]

qps = [20,32,43,55]

OPT = 0 # optimizacoes ligadas = 1
gprof = 1

threads = 4 # numero de processos em parelelo

taps = 8

#yuvs = [
#"DirtBike_426x240_24_120f_8bit_420.y4m",
# "RainHDRAmazon_1280x720_24_60f_10bit_420.y4m",
# "PanHDRAmazon_1920x1080_24_60f_10bit_420.y4m",
# "RushHour_1920x1080_25_60f_8bit_420.y4m",
# "WaterHDRAmazon_640x360_24_60f_10bit_420.y4m",
# "Shields2_640x360_50_120f_8bit_420.y4m",
# "ParkJoy_1920x1080_50_60f_8bit_420.y4m",
# "BQFree_426x240_60_120f_8bit_420.y4m",
# "PedestrianArea_1920x1080_25_60f_8bit_420.y4m",
# "TouchdownPass_1920x1080_30_60f_8bit_420.y4m",
# "NetflixTango_1280x720_60_120f_8bit_420.y4m",
# "FourPeople_1280x720_60_120f_8bit_420.y4m",
# "NetflixWindAndNature_4096x2160_60_60f_10bit_420.y4m",
# "Vidyo1_1280x720_60_120f_8bit_420.y4m",
# "NetflixBoat_1920x1080_60_60f_8bit_420.y4m",
# "Vidyo4_1280x720_60_120f_8bit_420.y4m",
# "Tacomanarrows_640x360_30_120f_8bit_420.y4m",
# "Station2_1920x1080_25_60f_8bit_420.y4m",
# "NetflixCrosswalk_1920x1080_60_60f_8bit_420.y4m",
# "NetflixFoodMarket_1920x1080_60_60f_8bit_420.y4m",
# "Hearthstone_1920x1080_60_60f_8bit_444.y4m",
# "NetflixNarrator_4096x2160_60_60f_10bit_420.y4m",
# "NetflixDancers_4096x2160_60_60f_10bit_420.y4m",
# "Life_1920x1080_30_60f_8bit_420.y4m",
# "Desktop2_640x360_30_120f_8bit_420.y4m",
# "Johnny_1280x720_60_120f_8bit_420.y4m",
# "DucksTakeOff_1920x1080_50_60f_8bit_420.y4m",
# "NetflixTunnelFlag_1920x1080_60_60f_8bit_420.y4m",
# "GuitarHDRAmazon_1920x1080_24_60f_10bit_420.y4m",
# "BQZoom_426x240_30_120f_8bit_420.y4m",
# "NetflixFoodMarket2_1280x720_60_120f_8bit_420.y4m",
# "NetflixBarScene_4096x2160_60_60f_10bit_420.y4m",
# "Dark_1280x720_30_120f_8bit_420.y4m",
# "BQHighway_426x240_60_120f_8bit_420.y4m",
# "Wikipedia_1920x1080_30_60f_8bit_420.y4m",
# "CrowdRun_1920x1080_50_60f_8bit_420.y4m",
# "SnowMnt_640x360_30_120f_8bit_420.y4m",
# "Aspen_1920x1080_30_60f_8bit_420.y4m",
# "SeaplaneHDRAmazon_1920x1080_24_60f_10bit_420.y4m",
# "NetflixRitualDance_4096x2160_60_60f_10bit_420.y4m",
# "BoatHDRAmazon_1280x720_24_60f_10bit_420.y4m",
# "NetflixRollerCoaster_1280x720_60_120f_8bit_420.y4m",
# "NetflixPierSeaside_1920x1080_60_60f_8bit_420.y4m",
# "NetflixDinnerScene_1280x720_60_120f_8bit_420.y4m",
# "ControlledBurn_640x360_30_120f_8bit_420.y4m",
# "KristenAndSara_1280x720_60_120f_8bit_420.y4m",
# "Gipsrestat_1280x720_50_120f_8bit_420.y4m",
# "Niklas_640x360_30_120f_8bit_420.y4m",
# "RedKayak_640x360_30_120f_8bit_420.y4m",
# "Chairlift_426x240_24_120f_8bit_420.y4m",
# "SpeedBag_640x360_30_120f_8bit_420.y4m",
# "Mmstationary_640x480_30_120f_8bit_420.y4m",
# "EuroTruckSimulator2_1920x1080_60_60f_8bit_444.y4m",
# "StreetHDRAmazon_3840x2160_24_60f_10bit_420.y4m",
# "NetflixDrivingPOV_1280x720_60_120f_8bit_420.y4m",
# "CSGO_1920x1080_60_60f_8bit_444.y4m",
# "STARCRAFT_1920x1080_60_60f_8bit_420.y4m",
# "NetflixBoxingPractice_4096x2160_60_60f_10bit_420.y4m",
# "Rain2HDRAmazon_640x360_24_60f_10bit_420.y4m",
# "Riverbed_640x360_25_120f_8bit_420.y4m",
# "NetflixToddlerFountain_4096x2160_60_60f_10bit_420.y4m",
# "NetflixAerial_1920x1080_60_60f_8bit_420.y4m",
# "Stockholm_640x360_60_120f_8bit_420.y4m",
# "NetflixSquareAndTimelapse_1920x1080_60_60f_8bit_420.y4m",
# "BlueSky_640x360_25_120f_8bit_420.y4m",
# "OldTownCross_1920x1080_50_60f_8bit_420.y4m",
# "Vidyo3_1280x720_60_120f_8bit_420.y4m",
# "MINECRAFT_1920x1080_60_60f_8bit_420.y4m",
# "Mozzoom_426x240_30_120f_8bit_420.y4m",
# "PVQSlideshow_1920x1080_30_60f_8bit_444.y4m",
# "RushFieldCuts_1920x1080_30_60f_8bit_420.y4m",
# "Thaloundeskmtg_640x360_30_120f_8bit_420.y4m",
# "Kirland_640x360_30_120f_8bit_420.y4m",
# "DOTA2_1920x1080_60_60f_8bit_420.y4m"
#] 

#yuvs=["Campfire_3840x2160_30fps_10bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv"]#ClasseA1

#yuvs=["ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]#ClasseA2

#yuvs=["BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv"]#ClasseB

#yuvs=["RaceHorses_832x480_30fps_8bit_420","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"]#ClasseC

#yuvs=["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30fps_8bit_420.yuv"]#ClasseD

#yuvs=["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv"]#ClasseE

#yuvs=[ArenaOfValor_1920x1080_60fps_8bit_420.yuv,"BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30.yuv"]#ClasseF


#yuvsvvc = ["MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","ArenaOfValor_1920x1080_60fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]#,"CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv"]	#VVC

#yuvshevc = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"]	#VVC_HEVC


#yuvs = os.listdir("/home/icaro/Videos/av1_sets")
#for i in range(len(yuvs)):
#	print(yuvs[i])

outpath = "/home/grellert/output_av1"
outpath = "/home/icaro/output_av1"

encpath = "/home/grellert/pesquisa_av1"
encpath = "/home/icaro/av1_pesquisa/aom"

yuvpath = "/home/icaro/Videos/av1_sets"

shpath = "../aom"
filename = "run_av1.sh"

try:
	os.system("mkdir ../aom")
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
bina = "aomenc"

if taps == 8:
	taps = ""
else:
	taps = "--fme_filter_ntaps=%s"%taps
	inf = inf + "_" + "taps"

if gprof == 0:
	#bina = "EncoderAppStatic_std"
	binpath = "%s/build"%encpath

else:
	binpath = "%s/build_d"%encpath
	inf = inf + "_" + "gprof"

if OPT == 1:
	#simd = "AVX2"
	inf = inf + "_" + "OPT"
	binpath = binpath + "_OPT"

else:
	#simd = "SCALAR"
	inf = inf + "_" + "noOPT"
	binpath = binpath + "_noOPT"

file = open("./%s/%s"%(shpath,filename),"w")

for yuv in yuvs:
	for qp in qps:

		try:
			vid,pix,fr,fl,b,dummy = yuv.split("_")
			b = b.strip("bit")
			fr = fr.strip("fps")
			nome = vid+"_"+pix+"_"+fr+"fps_"+b+"bit"
			w,h = pix.split("x")

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

			if int(w)*int(h) < 8294400:
				b = "8"
			else:
				b = "10"

			nome = nome+b+"bit"

		info = "%sqp_%sframes"%(qp,f) + inf

		#linha = "%s/%s -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b %s -o %s/bin/%s_%s.bin %s/%s 2> %s/out/%s_%s.txt"%(binpath,bina,w,h,qp-3,qp+5,f,b,outpath,nome,info,yuvpath,yuv,outpath,nome,info)
		
		linha = "%s/%s -w %s -h %s -codec=av1 -ivf -frame-parallel=0 -tile-columns=0 -cpu-used=0 -threads=1 --cq-level=%s --limit=%s -b %s -o %s/bin/%s_%s.bin %s/%s 2> %s/out/%s_%s.txt"%(binpath,bina,w,h,qp,f,b,outpath,nome,info,yuvpath,yuv,outpath,nome,info)

		linha0 =  "echo \"%s_%s DONE!\"\n"%(nome,info)

		if gprof == 1:

			linha2 = "mv ./gmon.out %s/gmon/gmon_%s_%s.out "%(outpath,nome,info)

			linha3 = "gprof %s/%s %s/gmon/gmon_%s_%s.out > %s/gprof/%s_%s.txt"%(binpath,bina,outpath,nome,info,outpath,nome,info)

			#VERIFICAR SOBRESCRICAO
			try:
				test = open("%s/%s/out/%s_%s.txt"%(homepath,outpath,nome,info),"r")
				tlines = test.readlines()
				tline = tlines[-1]
				if "Total Time" not in tline:
					file.write(linha + " && " + linha2 + " && " + linha3 + " && " + linha0 + "\n")
			except:
				file.write(linha + " && " + linha2 + " && " + linha3 + " && " + linha0 + "\n")

		else:
			linha = "{ time %s/%s -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b %s -o %s/bin/%s_%s.bin %s/%s 2> %s/out/%s_%s.txt"%(binpath,bina,w,h,qp-3,qp+5,f,b,outpath,nome,info,yuvpath,yuv,outpath,nome,info)

			try:
				test = open("%s/out/%s_%s.txt"%(outpath,nome,info),"r")
				tlines = test.readlines()
				tline = tlines[-1]
				if "Total Time" not in tline:
					file.write(linha + " && " + linha0 + "\n")
			except:
				file.write(linha + " && " + linha0 + "\n")

i=0
if threads >= 1:

	file = open("%s/%s"%(shpath,filename),"r")

	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)
	#nconf = len(confs)

	for x in range(threads):

		try:
			os.system("mkdir %s/script%d"%(shpath,x+1))
		except:
			pass
		file2 = open("%s/script%d/%d%s.sh"%(shpath,x+1,x+1,inf),"w")
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
