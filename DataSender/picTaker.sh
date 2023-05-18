while :
do
	fswebcam -D 2 -S 20 --set brightness=30% --set contrast=0% -F 4 -r 1280x720 --no-banner LatestPicture.jpg
	sleep 1
done
