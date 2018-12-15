def factors(n):
    """Returns sorted factors of a number"""
    from functools import reduce;
    return sorted(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def show_slices(slices):
    """show n slices of image in a well shaped grid"""
    import matplotlib.pyplot as plt;
    
    def get_subplot_dim(n):
        f = factors(n)
        return f[len(f)//2 - 1:len(f)//2 + 1]

    def make_axes(ax,slice):
        ax.imshow(slice, cmap='gray', origin='lower')
        ax.set_axis_off()
        ax.autoscale_view('tight')
        return ax;
    
    nslices = len(slices)
    nrows, ncols = get_subplot_dim(nslices)
    maxcols = 10
    if ncols > maxcols:
        ncols = maxcols
        nrows = nslices//maxcols + 1
    print('nrows: {}, ncols: {}, nslices: {}'.format(nrows, ncols, nslices))
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols,nrows))
    for i in range(nrows*ncols):
        row = i//ncols
        col = i%ncols
        if i < len(slices):
            slice = slices[i].T
            if nrows == 1:
                axes[col] = make_axes(axes[col], slice)
            else:
                axes[row, col] = make_axes(axes[row, col], slice)
        else:
            axes[row, col].axis('off')
    plt.savefig('a.pdf')
    plt.show()

def plot_dim(data, dim):
    if dim not in range(3):
        raise ValueError('Dim {} not in range 0, 1, 2.'.format(dim))
    slices = []
    for i in range(data.shape[dim]):
        if dim == 0:
            slice = data[i, :, :]
        elif dim == 1:
            slice = data[:, i, :]
        elif dim == 2:
            slice = data[:, :, i]
        slices.append(slice)
    show_slices(slices)

def print_shape(df):
    print('shape={}'.format(df.shape))