/home/icaro/hm/bin/TAppEncoderStatic -c /home/icaro/hm/cfg/encoder_randomaccess_main.cfg --InputFile="/home/icaro/origCfP/Traffic_2560x1600_30_crop.yuv" -fr 30 --SourceWidth=2560 --SourceHeight=1600 -q 37 -f 200 --fme_filter_ntaps=2 -b 8 --BitstreamFile="/home/icaro/pesquisa_ucpel/output_HM/local/bin/Traffic_2560x1600_30_2taps_37qp_200fframes_RA_.bin" > /home/icaro/pesquisa_ucpel/output_HM/local/out/Traffic_2560x1600_30_2taps_37qp_200fframes_RA_.txt && echo "Traffic_2560x1600_30_2taps_37qp_200fframes_RA_ DONE!" && cd /home/icaro/pesquisa_ucpel && sh git_upl.sh

cd /home/icaro/pesquisa_ucpel && sh git_upl.sh || true
