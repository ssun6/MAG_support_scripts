for f in */bins/*.fa;
    do f1=${f%%/bins/*.fa};
       f3="$(cut -d'_' -f1 <<<$f1)"
       f2=$(basename $f)
       s=${f1}/bins/${f3}_${f2};
       mv $f $s
done

for f in *.fa;
    do f1=${f:0:8}
       f2="$(cut -d'b' -f2 <<<$f)"
       s=${f1}_b${f2}
       mv $f $s
done

find . -name "CheckM.txt" -type f -print -exec cat {} \; > all_checkM.txt
