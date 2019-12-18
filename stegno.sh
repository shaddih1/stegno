append() {
    echo $TEXT >> $FNAME
}

extract(){
    TEXT=$(strings $FNAME | tail -1)
    echo "Text: $TEXT"
}

echo "[1] Hide text inside image"
echo "[2] Extract hidden text from image"
printf "\nChose option: "
read option

if [ $option == "1" ]; then
	printf "File name: "
	read FNAME

	printf "Text: "
	read TEXT
	append
	echo "Text has be hidden inside the image"
elif [ $option == "2" ]; then
	printf "File name: "
	read FNAME

	extract
else
	echo "Invalid option"
fi
