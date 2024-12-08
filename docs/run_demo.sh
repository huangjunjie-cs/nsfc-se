xelatex 青年2024.tex
bibtex 青年2024
xelatex 青年2024.tex
xelatex 青年2024.tex

cp 青年2024.tex 青年2024-se.tex
sed -i 's/\\usepackage[windows]{nsfc}/\\usepackage[windows]{nsfc_se}/' 青年2024-se.tex
xelatex 青年2024-se.tex
bibtex 青年2024-se
xelatex 青年2024-se.tex
xelatex 青年2024-se.tex

