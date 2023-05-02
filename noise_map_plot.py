filepath = os.path.join('decomposition_grs', 'gpy_maps', 'grs-test_field_noise_map.fits')
noise = fits.getdata(filepath)
wcs = WCS(fits.getheader(filepath))

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(projection=wcs))

img_noise = ax.imshow(noise, cmap='plasma_r', vmin=0.075, vmax=0.375)
fig.colorbar(img_noise, ax=ax, extend='max')
ax.set_title('Noise map')
add_style(ax)

plt.show()
