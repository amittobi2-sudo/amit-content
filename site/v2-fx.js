/* v2 fx layer: Motion (motion.dev) + Anime.js. Progressive: does nothing if libraries fail to load or reduced motion is on. */
(()=>{
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
const M=window.Motion, A=window.anime;
/* 1. Headline word-by-word spring reveal (Motion) */
if(M&&M.animate&&M.inView){
  const {animate,inView,stagger}=M;
  document.querySelectorAll('.h2, body.inner main h2, .phero h1').forEach(h=>{
    if(h.closest('.mani'))return;
    h.removeAttribute('data-r');h.classList.add('in');
    const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.append(t);return}const s=document.createElement('span');s.className='fxw';s.style.display='inline-block';s.style.opacity='0.001';s.textContent=t;f.append(s)});c.replaceWith(f)}else if(c.nodeType===1)walk(c)})};
    walk(h);
    inView(h,()=>{const ws=h.querySelectorAll('.fxw');try{animate(ws,{opacity:[0,1],y:[28,0],filter:['blur(10px)','blur(0px)']},{duration:.9,delay:stagger(.06),ease:[.16,1,.3,1]})}catch(err){ws.forEach(w=>w.style.opacity='1')}setTimeout(()=>ws.forEach(w=>{if(getComputedStyle(w).opacity<.5)w.style.opacity='1'}),2500)},{margin:'0px 0px -10% 0px'});
  });
  /* 2. cards lift in with spring */
  document.querySelectorAll('.card,.case,.chap,.q').forEach(c=>{
    inView(c,()=>{animate(c,{scale:[.96,1]},{type:'spring',stiffness:180,damping:18})},{margin:'0px 0px -8% 0px'});
  });
  /* 3. hero tagline letter shimmer */
  const tag=document.querySelector('.hero .tag em');
  if(tag){animate(tag,{backgroundPositionX:['200%','-200%']},{duration:4,repeat:Infinity,ease:'linear'});
    Object.assign(tag.style,{backgroundImage:'linear-gradient(90deg,#E0263F 0%,#ff8a98 50%,#E0263F 100%)',backgroundSize:'200% 100%',WebkitBackgroundClip:'text',backgroundClip:'text',color:'transparent'});}
}
/* 4. Anime.js: business grid ripple from center + 360 wheel draw */
if(A){
  document.querySelectorAll('.biz .bz,.gallery figure,.wheel .node').forEach(x=>x.style.opacity='0');
  const biz=document.querySelector('.biz');
  if(biz){const io=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;io.disconnect();
    A({targets:biz.querySelectorAll('.bz'),opacity:[0,1],translateY:[40,0],scale:[.9,1],delay:A.stagger(90,{grid:[4,2],from:'center'}),duration:900,easing:'easeOutExpo'})},{threshold:.2});io.observe(biz)}
  const gal=document.querySelector('.gallery');
  if(gal){const io2=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;io2.disconnect();
    A({targets:gal.querySelectorAll('figure'),opacity:[0,1],translateY:[50,0],delay:A.stagger(80),duration:1000,easing:'easeOutExpo'})},{threshold:.1});io2.observe(gal)}
  const ring=document.querySelector('.wheel svg');
  if(ring){const io3=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;io3.disconnect();
    A({targets:ring.querySelectorAll('.node'),scale:[0,1],opacity:[0,1],delay:A.stagger(70),duration:700,easing:'easeOutBack'})},{threshold:.3});io3.observe(ring)}
}
})();
