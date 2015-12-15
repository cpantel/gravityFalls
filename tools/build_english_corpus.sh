#build english corpus
strings /var/lib/aspell/en-common.rws | grep -ve "@" -ve "*" -ve "^[0123456789]" -ve ".*'s$" -ve '[[:upper:]]' | sed -e 's/^\t//'  | sort > english_corpus.txt