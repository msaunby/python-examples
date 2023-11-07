# def fence(original, wrapper):
#     fenced = wrapper + original + wrapper
#     return fenced

fence = lambda original, wrapper: wrapper + original + wrapper

print(fence('hi', '**'))
