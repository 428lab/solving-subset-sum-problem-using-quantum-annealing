import numpy as np
from dwave.system import DWaveSampler, EmbeddingComposite
import os
import argparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access token
TOKEN = os.getenv('D_WAVE_TOKEN')

class SubsetSumSolver:
    def __init__(self, N, target, lam, annealing_time, dwave_config):
        self.N = N
        self.target = target
        self.lam = lam
        self.dwave_config = dwave_config
        self.sampler = EmbeddingComposite(DWaveSampler(**dwave_config))
        self.Q = self._initialize_qubo()

        # サンプリングパラメータの設定
        self.num_reads = 1000  # 試行回数を増やす
        self.annealing_time = annealing_time  # アニーリング時間を調整する


    def _initialize_qubo(self):
        """初期化と目的関数の二次係数の計算"""

        # QUBO行列を構築する
        Q = np.zeros((self.N, self.N))

        # 目的関数の二次項と線形項の計算
        for i in range(self.N):
            for j in range(self.N):
                Q[i, j] = (i+1) * (j+1) * self.lam # i+1 and j+1 because we're working with numbers 1 to 100

        # 目的関数の線形項を引く
        linear_term = -1000 * np.arange(1, self.N+1)  * self.lam

        # 対角要素（線形項）に加算
        np.fill_diagonal(Q, Q.diagonal() + linear_term)

        return Q

    def solve(self):
        """QUBOを解く"""
        sampleset = self.sampler.sample_qubo(self.Q, num_reads=1000, label='Subset Sum with lam: ' + str(self.lam), annealing_time=self.annealing_time)
        return sampleset

    def print_solutions(self, sampleset):
        """解の表示"""
        for sample in sampleset.lowest().samples():
            solution = [i+1 for i in range(self.N) if sample[i] == 1]
            if sum(solution) == self.target:
                print("Found exact solution:", solution)
            else:
                print("Found solution with deviation:", solution, "Sum:", sum(solution))

    def save_sampleset(self, sampleset, filename='sampleset.npy'):
        """サンプルセットの保存"""
        np.save(filename, sampleset)

dwave_config = {
    'endpoint': 'https://cloud.dwavesys.com/sapi',
    'token': TOKEN,
    'solver': 'Advantage_system4.1'
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--annealing-time', default=40, type=int, help='D-Wave annealing time in micro second')
    parser.add_argument('--penalty-scale', default=10, type=int, help='objective function coefficients')

    opt = parser.parse_args()
    print(opt)

    # アニーリング時間
    annealing_time = opt.annealing_time

    # 目的関数の係数
    penalty_scale = opt.penalty_scale

    # 1から50（N）の数字の中から数字を最大1回ずつ選択して合計が500（target）になる組み合わせをできるだけ見つける
    solver = SubsetSumSolver(N=50, target=500, lam=penalty_scale ,annealing_time=annealing_time, dwave_config=dwave_config)
    sampleset = solver.solve()
    solver.print_solutions(sampleset)
    solver.save_sampleset(sampleset, filename='sampleset_annealing_time' + str(annealing_time) + '_lambda' + str(penalty_scale) + '.npy')

