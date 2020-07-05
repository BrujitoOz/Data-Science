# Comprime una imagen bmp a formato jpeg
from pylab import gcf
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfile
from matplotlib.pyplot import figure, cm, show, imshow, axis, savefig, get_current_fig_manager, subplots_adjust
from utils import is_greyscale, transform, reconstruct, mergeChannelsToImg

# Get .bmp image from files explorer
root = Tk()
root.withdraw()
original = askopenfile(filetypes = [('.bmp files', '.bmp')])
original = Image.open(original.name)
root.destroy()

# Wavelet haar aplication
if is_greyscale(original):
    coeefs = transform(original)
    reconstructedImg = reconstruct(coeefs)
else:
    redImg = original.split()[0].convert('L')
    greenImg = original.split()[1].convert('L')
    blueImg = original.split()[2].convert('L')
    coefsRed = transform(redImg)
    coefsGreen = transform(greenImg)
    coefsBlue = transform(blueImg)
    reconstructedRed = reconstruct(coefsRed)
    reconstructedGreen = reconstruct(coefsGreen)
    reconstructedBlue = reconstruct(coefsBlue)
    reconstructedImg = mergeChannelsToImg(reconstructedRed, reconstructedGreen, reconstructedBlue)

# Compare results
plotImg = figure()
plotImg = gcf()
plotImg.canvas.set_window_title("Compare results")
ax = plotImg.add_subplot(1, 2,  1)
ax.imshow(original, cmap = cm.gray)
ax.axis("off")
ax.set_title("Original", fontsize = 12)
ax = plotImg.add_subplot(1, 2, 2)
ax.imshow(reconstructedImg, cmap = cm.gray)
ax.axis("off")
ax.set_title("Reconstructed", fontsize = 12)

# Show image
a, l = original.size
fig = figure(figsize=(a * 0.0104166667, l * 0.0104166667))
subplots_adjust(wspace=0, hspace=0,left=0.0,top=1.0,right=1.0,bottom=0.0)
fig = gcf()
fig.canvas.set_window_title('Haar Compress')
imshow(reconstructedImg, cmap = cm.gray)
axis("off")
show()