if iwgetid | grep -q 'ESSID'; then
  echo "matched"
else
 echo "Lost Connection"
fi
