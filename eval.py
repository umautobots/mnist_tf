#! /usr/bin/python3
import os
from glob import glob
import argparse
from tensorflow import keras
import util

parser = argparse.ArgumentParser()
parser.add_argument('--idx_ckpt', type=int, default=-1,
                    help='Index of the checkpoint to load. (default: -1)')
parser.add_argument('--fashion', dest='fashion', action='store_true')
args = parser.parse_args()

if args.fashion:
    mnist = keras.datasets.fashion_mnist
else:
    mnist = keras.datasets.mnist

_, (x_test, y_test) = mnist.load_data()

util.allow_gpu_memory_growth()

model = util.build_model()
model.compile(
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

checkpoints = sorted(glob('checkpoints/*'))

[print(f'{idx}: {ckpt}') for idx, ckpt in enumerate(checkpoints)]
print(f'Loading {checkpoints[args.idx_ckpt]}')
model.load_weights(os.path.join(checkpoints[args.idx_ckpt], 'cp.ckpt'))

loss, acc = model.evaluate(x_test, y_test, verbose=0)

print(f'Restored model: accuracy = {100 * acc:5.2f}%')