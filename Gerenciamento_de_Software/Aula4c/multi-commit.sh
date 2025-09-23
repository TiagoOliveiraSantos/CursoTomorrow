git add .

for file in $(git diff --cached --name-only); do
	echo "Digite a mensagem do commit para o arquivo: $file"
	read msg
	git commit -m "$msg" -- "$file"
done
