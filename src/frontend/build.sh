rm index.html
echo '<!DOCTYPE html>' >> index.html
echo '<html lang="en">' >> index.html
echo '<head>' >> index.html
echo '<meta charset="UTF-8">' >> index.html
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">' >> index.html
echo '<title>Document</title>' >> index.html
# echo "<link rel='icon' type='image/x-icon' href='data:image/png;base64,$(cat ../../sombrero-small.png | base64)'>" >> index.html
echo '</head>' >> index.html
echo '<body>' >> index.html
echo '<canvas id="canvas" width="500" height="500"></canvas>' >> index.html
echo '<script>' >> index.html
bun build index.ts >> index.html
echo '</script>' >> index.html
echo '</body>' >> index.html
echo '</html>' >> index.html