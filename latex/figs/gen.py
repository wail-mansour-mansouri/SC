import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.grid':True,'grid.alpha':0.3,
    'figure.autolayout':True})
INSEA=(0,0.30,0.50); VERT=(0,0.47,0.27); OR=(0.74,0.35,0)
rng=np.random.default_rng(7)

def ar_sim(phis, n=300, sigma=1.0, c=0.0, burn=200, seed=1):
    r=np.random.default_rng(seed); p=len(phis); x=np.zeros(n+burn)
    e=r.normal(0,sigma,n+burn)
    for t in range(p,n+burn):
        x[t]=c+sum(phis[j]*x[t-1-j] for j in range(p))+e[t]
    return x[burn:]

def acf_theo_ar1(phi,K): return np.array([phi**k for k in range(K+1)])

# 1) AR(1) trajectories
fig,ax=plt.subplots(1,3,figsize=(11,3))
for a,(phi,ttl) in zip(ax,[(0.8,r'$\phi=0.8$ (persistant)'),(-0.8,r'$\phi=-0.8$ (oscillant)'),(0.3,r'$\phi=0.3$ (faible)')]):
    a.plot(ar_sim([phi],150,seed=3),color=INSEA,lw=0.9)
    a.set_title(ttl); a.set_xlabel('t')
fig.savefig('ar1_traj.pdf'); plt.close(fig)

# 2) ACF of AR(1) positive & negative
fig,ax=plt.subplots(1,2,figsize=(9,3))
K=15
for a,(phi,ttl) in zip(ax,[(0.8,r'AR(1), $\phi=0.8$'),(-0.8,r'AR(1), $\phi=-0.8$')]):
    ks=np.arange(0,K+1); r=acf_theo_ar1(phi,K)
    a.stem(ks,r,linefmt='-',markerfmt='o',basefmt=' ')
    a.axhline(0,color='k',lw=0.6); a.set_title(ttl); a.set_xlabel('k'); a.set_ylabel(r'$\rho(k)$')
    a.set_ylim(-1.05,1.05)
fig.savefig('acf_ar1.pdf'); plt.close(fig)

# helper theoretical ACF for AR(2) via Yule-Walker recursion
def acf_ar2(phi1,phi2,K):
    rho=[1.0, phi1/(1-phi2)]
    for k in range(2,K+1):
        rho.append(phi1*rho[-1]+phi2*rho[-2])
    return np.array(rho)
def pacf_from_acf(rho,K):
    # Durbin-Levinson
    pacf=[1.0]; phi=np.zeros((K+1,K+1))
    phi[1,1]=rho[1]; pacf.append(rho[1])
    for k in range(2,K+1):
        num=rho[k]-sum(phi[k-1,j]*rho[k-j] for j in range(1,k))
        den=1-sum(phi[k-1,j]*rho[j] for j in range(1,k))
        phi[k,k]=num/den
        for j in range(1,k): phi[k,j]=phi[k-1,j]-phi[k,k]*phi[k-1,k-j]
        pacf.append(phi[k,k])
    return np.array(pacf)

# 3) AR(2) ACF + PACF  (phi1=0.5, phi2=0.3) -> stationary
phi1,phi2=0.5,0.3; K=15
rho=acf_ar2(phi1,phi2,K); pac=pacf_from_acf(rho,K)
fig,ax=plt.subplots(1,2,figsize=(9,3))
ax[0].stem(range(K+1),rho,basefmt=' '); ax[0].set_title(r'ACF AR(2) $\phi_1=0.5,\phi_2=0.3$')
ax[0].set_xlabel('k'); ax[0].set_ylabel(r'$\rho(k)$'); ax[0].axhline(0,color='k',lw=.6)
ax[1].stem(range(K+1),pac,basefmt=' ',linefmt=VERT and '-'); ax[1].set_title('PACF (coupe après k=2)')
ax[1].set_xlabel('k'); ax[1].set_ylabel('P(k)'); ax[1].axhline(0,color='k',lw=.6)
for a in ax: a.set_ylim(-0.4,1.05)
fig.savefig('acfpacf_ar2.pdf'); plt.close(fig)

# 4) MA(1) ACF + PACF (theta=0.8 in X=a+theta a_{t-1})
th=0.8; K=15
rho_ma=np.zeros(K+1); rho_ma[0]=1; rho_ma[1]=th/(1+th**2)
pac_ma=pacf_from_acf(rho_ma,K)
fig,ax=plt.subplots(1,2,figsize=(9,3))
ax[0].stem(range(K+1),rho_ma,basefmt=' '); ax[0].set_title(r'ACF MA(1) $\theta=0.8$ (coupe après k=1)')
ax[0].set_xlabel('k'); ax[0].set_ylabel(r'$\rho(k)$'); ax[0].axhline(0,color='k',lw=.6)
ax[1].stem(range(K+1),pac_ma,basefmt=' '); ax[1].set_title('PACF (décroît)')
ax[1].set_xlabel('k'); ax[1].set_ylabel('P(k)'); ax[1].axhline(0,color='k',lw=.6)
for a in ax: a.set_ylim(-0.6,1.05)
fig.savefig('acfpacf_ma1.pdf'); plt.close(fig)

# 5) Non-stationary: random walk traj + slow ACF decay
fig,ax=plt.subplots(1,2,figsize=(9,3))
rw=np.cumsum(rng.normal(0,1,300))
ax[0].plot(rw,color=OR,lw=0.9); ax[0].set_title('Marche aléatoire (I(1))'); ax[0].set_xlabel('t')
# empirical ACF of rw
def acf_emp(x,K):
    x=x-x.mean(); d=np.sum(x**2); return np.array([1.0]+[np.sum(x[k:]*x[:-k])/d for k in range(1,K+1)])
ax[1].stem(range(0,21),acf_emp(rw,20),basefmt=' '); ax[1].set_title('ACF empirique (décroissance lente $\\approx 1$)')
ax[1].set_xlabel('k'); ax[1].set_ylabel(r'$\hat\rho(k)$'); ax[1].axhline(0,color='k',lw=.6); ax[1].set_ylim(-0.1,1.05)
fig.savefig('nonstat.pdf'); plt.close(fig)

# 6) Decomposition: trend+season+noise additive
n=48; t=np.arange(n); trend=10+0.6*t; season=8*np.sin(2*np.pi*t/12); noise=rng.normal(0,2,n)
X=trend+season+noise
fig,ax=plt.subplots(4,1,figsize=(8,7),sharex=True)
ax[0].plot(t,X,color=INSEA); ax[0].set_ylabel(r'$X_t$'); ax[0].set_title('Série observée = Tendance + Saisonnalité + Résidu (additif)')
ax[1].plot(t,trend,color=OR); ax[1].set_ylabel(r'$T_t$')
ax[2].plot(t,season,color=VERT); ax[2].set_ylabel(r'$S_t$')
ax[3].plot(t,noise,color='gray'); ax[3].set_ylabel(r'$E_t$'); ax[3].set_xlabel('t (mois)')
fig.savefig('decomposition.pdf'); plt.close(fig)

# 7) Forecast fan chart for AR(1)
phi=0.7; sig=1; mu=0; Xn=3.0; H=10
fc=[Xn]; var=[0]
for h in range(1,H+1):
    fc.append(mu+phi*(fc[-1]-mu)); var.append(sig**2*sum(phi**(2*j) for j in range(h)))
fc=np.array(fc[1:]); sd=np.sqrt(var[1:])
hist=ar_sim([phi],40,seed=5)+0  # arbitrary history
fig,ax=plt.subplots(figsize=(8,3.2))
ax.plot(range(-40,0),hist,color=INSEA,lw=0.9,label='observé')
ax.plot(range(0,H),fc,'o-',color=OR,label='prévision')
ax.fill_between(range(0,H),fc-1.96*sd,fc+1.96*sd,color=OR,alpha=0.2,label='IC 95%')
ax.axhline(mu,ls='--',color='gray',lw=0.8); ax.legend(); ax.set_xlabel('horizon'); ax.set_title('Prévision AR(1) et bande de confiance (élargissement avec h)')
fig.savefig('forecast.pdf'); plt.close(fig)

# 8) Series to identify (Q I.1): 6 series
fig,ax=plt.subplots(3,2,figsize=(10,7))
n=60; t=np.arange(n); s=5*np.sin(2*np.pi*t/12); f=8*np.sin(2*np.pi*t/40); a=20; eps=rng.normal(0,1,n)
panels=[(eps,r'(1) $y_t=\varepsilon_t$'),
        (s+eps,r'(2) $y_t=s_t+\varepsilon_t$'),
        (a+s+eps,r'(3) $y_t=a+s_t+\varepsilon_t$'),
        (a*s*np.abs(eps)/2+a,r'(4) $y_t=a\,s_t\,\varepsilon_t$ (multiplicatif)'),
        (f+eps,r'(5) $y_t=f_t+\varepsilon_t$'),
        (f*eps,r'(6) $y_t=f_t\,\varepsilon_t$')]
for axx,(y,ttl) in zip(ax.ravel(),panels):
    axx.plot(t,y,color=INSEA,lw=0.9); axx.set_title(ttl,fontsize=10)
fig.savefig('identif_series.pdf'); plt.close(fig)

# 9) Three ACF for Series D,E,F (Q I.2): AR-decay, MA cutoff, non-stationary
fig,ax=plt.subplots(1,3,figsize=(11,3)); K=18
rhoD=acf_theo_ar1(0.7,K)  # AR(1)
rhoE=np.zeros(K+1); rhoE[0]=1; rhoE[1]=0.45; rhoE[2]=-0.3  # MA(2) like
rhoF=acf_emp(np.cumsum(rng.normal(0,1,200)),K)  # nonstationary
for a,(r,ttl) in zip(ax,[(rhoD,'Série D'),(rhoE,'Série E'),(rhoF,'Série F')]):
    a.stem(range(K+1),r,basefmt=' '); a.set_title(ttl); a.set_xlabel('k'); a.axhline(0,color='k',lw=.6); a.set_ylim(-0.6,1.05)
fig.savefig('identif_acf.pdf'); plt.close(fig)

# 10) MM smoothing illustration
fig,ax=plt.subplots(figsize=(8,3))
n=48; t=np.arange(n); X=10+0.4*t+6*np.sin(2*np.pi*t/4)+rng.normal(0,1.5,n)
mm=np.convolve(np.r_[X[0],X[0],X,X[-1],X[-1]],[1/8,1/4,1/4,1/4,1/8],'valid')
ax.plot(t,X,color=INSEA,lw=0.9,label='série brute (saison période 4)')
ax.plot(t,mm,color=OR,lw=2,label='MM4 centrée (tendance)')
ax.legend(); ax.set_xlabel('t'); ax.set_title('La MM4 absorbe la saisonnalité de période 4 et conserve la tendance')
fig.savefig('mm4.pdf'); plt.close(fig)

print("ALL FIGURES OK")
