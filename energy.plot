set terminal pngcairo enhanced color lw 1.5 font 'Times Roman'
set xrange [0.00:1.00]
set yrange [300:1500]
set output "energy.png"
set xlabel "lambda"
set ylabel "energy ((micro joule per bit))"
set key right top vertical
plot "energy.dat" title "energy (micro joule per bit)" with lines lw 1.5 lc 'blue',
