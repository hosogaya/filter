import numpy as np
import copy

class Particle:
    def __init__(self, xdim, zdim) -> None:
        self.x = np.zeros((xdim, 1))
        self.z = np.zeros((zdim, 1))
        self.liklihood = 1.0

class ParticleFilter:
    def __init__(self, num, cov_v, cov_w, f, h) -> None:
        self.xdim, _ = cov_v.shape
        self.zdim, _ = cov_w.shape
        self.num = num
        self.pars = []# particles
        for i in range(self.num) : self.pars.append(Particle(self.xdim, self.zdim))
        self.cov_v = cov_v
        self.cov_w = cov_w
        
        self.x = np.zeros_like(self.pars[0].x)
        
        self.f = f
        self.h = h
    
    def generate(self, cov):
        """_summary_
            generate white noize from covariance matrix
        Args:
            cov (_type_): covariance matrix

        Returns:
            _type_: white noize 
        """
        n,_ = cov.shape
        noize =  np.array([np.random.multivariate_normal(np.zeros(n), cov)]).T
        return noize
    
    def predict(self, x, u, cov):
        """_summary_
            predict next state with prediction model and white noize
        Args:
            x (_type_): _description_ : current state
            u (_type_): _description_ : current input
            cov (_type_): _description_ : covarriance matrix
        """
        return self.f(x, u) + self.generate(cov)
    
    def liklihood(self, x, z, cov):
        return np.exp(-0.5*np.dot((self.h(x)-z).T, np.dot(np.linalg.inv(cov), self.h(x) - z)))
    
    def update(self):
        s = sum([par.liklihood for par in self.pars])
        for par in self.pars: par.liklihood /= s  # normalize
        self.x = np.zeros((self.xdim, 1))
        for par in self.pars:
            self.x += par.x * par.liklihood
    
    def resampling(self):
        cum = np.cumsum([par.liklihood for par in self.pars])
        cum = np.float64(cum/cum[-1]*self.num)
        thre = 1
        new_par = []
        for i in range(self.num):
            if cum[i] >= thre:
                for j in range(int(thre-1), int(np.round(cum[i])), 1):
                    new_par.append(Particle(self.xdim, self.zdim))
                    new_par[-1].x = self.pars[i].x
                    new_par[-1].liklihood = self.pars[i].liklihood
                thre = np.round(cum[i])+1
        
        self.pars = copy.deepcopy(new_par)          
            
    def one_step(self, u, z):
        for par in self.pars: par.x = self.predict(par.x, u, self.cov_v)
        for par in self.pars: par.liklihood = self.liklihood(par.x, z, self.cov_w)
        self.update()
        self.resampling()
        
def main():
    cov_v = np.array([[0.8, 0.8, 0.0, 0.0],
                      [0.0, 0.8, 0.0, 0.0],
                      [0.0, 0.0, 0.1, 0.0],
                      [0.0, 0.0, 0.0, 1.0]])
    cov_w = np.array([[0.8, 0.0], 
                      [0.0, 0.2]])
    
    dt = 0.1
    lf = 1.2
    lr = 1.2
    def f(x, u):
        xn = copy.deepcopy(x)
        beta = np.arctan(lr/(lf+lr)*np.tan(u[1][0]))
        xn[0][0] = x[0][0] + x[3][0]*dt*np.cos(x[2][0] + beta)
        xn[1][0] = x[1][0] + x[3][0]*dt*np.sin(x[2][0] + beta)
        xn[2][0] = x[2][0] + x[3][0]/lr*dt*np.sin(beta)
        xn[3][0] = x[3][0] + u[0][0]*dt
        return x; 
    
    lm = 10.*np.array([[np.cos(np.pi/20.), np.sin(np.pi/20.)]]).T
    def h(x):
        y = lm.T - x[:2]
        return np.array([[np.sqrt(y[0][0]**2 + y[1][0]**2), np.arctan2(y[1][0], y[0][0])]]).T
    
    pf = ParticleFilter(50, cov_v, cov_w, f, h)

    for i in range(5):
        u = np.array([[100., np.pi/18.]]).T
        z = np.array([[1.1, np.pi/20]]).T
        pf.one_step(u, z)
    
        print(pf.x)
    
    
    
if __name__ == "__main__":
    main()