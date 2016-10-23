# VideoSummarization
Course Project for CS771: Machine Learning

Use the following lines of code to download the SumMe dataset into the data folder. Refer to Michael Gygli's [page](https://people.ee.ethz.ch/~gyglim/vsum/).

```
chmod +x ./run_this.sh
./run_this.sh
```

Following is the list of dependencies: [imageio](https://imageio.github.io/), numpy, matplotlib, opencv3, tensorflow. 
```
sudo pip install imageio
```
The same goes for numpy, matplotlib, tensorflow. For opencv on Mac OSX,
```
brew install opencv3
brew install webp
```
The second command fixes an issue with importing opencv on Mac OSX.
