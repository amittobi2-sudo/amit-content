/* Amit Tobi v2 · motion layer (progressive enhancement: page is complete without this file) */
(()=>{
const d=document,root=d.documentElement,RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches;
root.classList.add('js');
const $=(s,c=d)=>c.querySelector(s),$$=(s,c=d)=>[...c.querySelectorAll(s)];
const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));

/* nav, progress, burger */
const nav=$('.nav'),prog=$('.progress');
const onScroll=()=>{const y=scrollY;nav&&nav.classList.toggle('scrolled',y>30);
  if(prog){const h=root.scrollHeight-innerHeight;prog.style.transform=`scaleX(${h>0?y/h:0})`}};
addEventListener('scroll',onScroll,{passive:true});onScroll();
const bg=$('.burger');bg&&bg.addEventListener('click',()=>{const o=nav.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
$$('.links a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));

/* cursor spotlight */
const spot=$('.spot');
if(spot&&FINE&&!RM){let tx=0,ty=0,x=0,y=0;d.body.classList.add('has-pointer');
  addEventListener('pointermove',e=>{tx=e.clientX;ty=e.clientY},{passive:true});
  (function l(){x+=(tx-x)*.12;y+=(ty-y)*.12;spot.style.transform=`translate(${x-310}px,${y-310}px)`;requestAnimationFrame(l)})();}

/* reveal */
$$('.stag').forEach(g=>[...g.children].forEach((c,i)=>c.style.setProperty('--i',i)));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -12% 0px'});
$$('[data-r],.stat,.case').forEach(el=>io.observe(el));

/* counters */
const fmt=n=>n.toLocaleString('en-US');
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);
  const el=e.target,to=+el.dataset.count,dur=RM?0:1800,t0=performance.now();
  const step=t=>{const p=dur?clamp((t-t0)/dur,0,1):1,v=Math.round(to*(1-Math.pow(1-p,4)));el.textContent=fmt(v);if(p<1)requestAnimationFrame(step)};
  requestAnimationFrame(step)}),{threshold:.5});
$$('[data-count]').forEach(el=>cio.observe(el));

/* hero intro */
if(!RM){$$('.hero h1 .ln>span').forEach((s,i)=>{s.animate([{transform:'translateY(105%)'},{transform:'none'}],{duration:1200,delay:150+i*120,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'})});
  $$('.hero [data-in]').forEach((s,i)=>s.animate([{opacity:.1,transform:'translateY(24px)'},{opacity:1,transform:'none'}],{duration:1100,delay:450+i*110,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'}));
  const pi=$('.portrait img');pi&&pi.animate([{opacity:.1,transform:'scale(1.08)'},{opacity:1,transform:'none'}],{duration:1800,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'});}

/* hero embers canvas */
const cv=$('.hero canvas');
if(cv&&!RM){const cx=cv.getContext('2d');let W,H,P=[],mx=-1e3,my=-1e3,run=true;const DPR=Math.min(devicePixelRatio||1,2);
  const size=()=>{W=cv.clientWidth;H=cv.clientHeight;cv.width=W*DPR;cv.height=H*DPR;cx.setTransform(DPR,0,0,DPR,0,0)};
  const N=()=>Math.round(clamp(W*H/9000,40,150));
  const mk=(y)=>({x:Math.random()*W,y:y??H+Math.random()*H*.3,r:Math.random()*1.8+.4,vy:-(Math.random()*.6+.15),vx:(Math.random()-.5)*.2,a:Math.random()*.6+.2,t:Math.random()*6.28});
  size();for(let i=0;i<N();i++)P.push(mk(Math.random()*H));
  addEventListener('resize',()=>{size()});
  cv.parentElement.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top},{passive:true});
  new IntersectionObserver(([e])=>{run=e.isIntersecting;if(run)loop()}).observe(cv);
  function loop(){if(!run)return;cx.clearRect(0,0,W,H);
    for(const p of P){p.t+=.02;p.x+=p.vx+Math.sin(p.t)*.15;p.y+=p.vy;
      const dx=p.x-mx,dy=p.y-my,dd=dx*dx+dy*dy;if(dd<14000){const f=(14000-dd)/14000*1.6;p.x+=dx/Math.sqrt(dd+1)*f;p.y+=dy/Math.sqrt(dd+1)*f}
      if(p.y<-10){Object.assign(p,mk())}
      const fade=clamp(p.y/H,0,1);cx.beginPath();cx.arc(p.x,p.y,p.r,0,6.283);
      cx.fillStyle=`rgba(${220+Math.round(35*fade)},${40+Math.round(40*(1-fade))},${60},${p.a*fade})`;cx.shadowColor='rgba(224,38,63,.9)';cx.shadowBlur=8;cx.fill()}
    requestAnimationFrame(loop)}
  loop();}

/* portrait parallax + badges */
const por=$('.portrait');
if(por&&!RM){addEventListener('scroll',()=>{const y=scrollY;if(y<innerHeight*1.2){por.style.transform=`translateY(${y*.18}px)`}},{passive:true})}

/* door / card spotlight + tilt */
$$('.door,.topic').forEach(c=>{if(!FINE||RM)return;
  c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),px=(e.clientX-r.left)/r.width,py=(e.clientY-r.top)/r.height;
    c.style.setProperty('--mx',px*100+'%');c.style.setProperty('--my',py*100+'%');
    c.style.transform=`perspective(900px) rotateX(${(.5-py)*6}deg) rotateY(${(px-.5)*8}deg) translateY(-4px)`});
  c.addEventListener('pointerleave',()=>{c.style.transform=''})});

/* magnetic buttons */
if(FINE&&!RM)$$('.btn').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.18}px,${(e.clientY-r.top-r.height/2)*.3}px)`});
  b.addEventListener('pointerleave',()=>{b.style.transform=''})});

/* manifesto word-by-word */
const bq=$('.mani blockquote');
if(bq){const hl=(bq.dataset.hl||'').split(',');
  const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.append(t);return}
      const s=d.createElement('span');s.className='w'+(hl.some(h=>h&&t.includes(h))?' hl':'');s.textContent=t;f.append(s)});c.replaceWith(f)}else walk(c)})};
  walk(bq);const ws=$$('.w',bq);
  if(RM){ws.forEach(w=>w.classList.add('on'))}else{
  const upd=()=>{const r=bq.getBoundingClientRect(),p=clamp((innerHeight*.85-r.top)/(r.height+innerHeight*.35),0,1),k=Math.floor(p*ws.length*1.05);ws.forEach((w,i)=>w.classList.toggle('on',i<k))};
  addEventListener('scroll',upd,{passive:true});upd();}}

/* pinned horizontal story */
const story=$('.story'),rail=$('.story .rail'),line=$('.story .line i');
if(story&&rail&&!RM){let dist=0;
  const setup=()=>{if(innerWidth<=1000){story.style.height='';rail.style.transform='';return}
    dist=rail.scrollWidth-innerWidth+80;story.style.height=(innerHeight+dist)+'px'};
  const upd=()=>{if(innerWidth<=1000)return;const r=story.getBoundingClientRect(),p=clamp(-r.top/(story.offsetHeight-innerHeight),0,1);
    rail.style.transform=`translateX(${p*dist}px)`;line&&(line.style.transform=`scaleX(${p})`)};
  setup();upd();addEventListener('resize',()=>{setup();upd()});addEventListener('scroll',upd,{passive:true});
  addEventListener('load',()=>{setup();upd()});}

/* 360 wheel */
const wheel=$('.wheel svg'),steps=$$('.steps li');
if(wheel&&steps.length){const n=steps.length,R=230,C=280,NS='http://www.w3.org/2000/svg';let html='';
  html+=`<circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="#26262B" stroke-width="1"/>`;
  html+=`<circle class="arc" cx="${C}" cy="${C}" r="${R}" fill="none" stroke="#C8102E" stroke-width="2" stroke-linecap="round" pathLength="100" stroke-dasharray="0 100" transform="rotate(-90 ${C} ${C})"/>`;
  for(let i=0;i<n;i++){const a=-Math.PI/2+i*2*Math.PI/n,x=C+R*Math.cos(a),y=C+R*Math.sin(a),lx=C+(R+38)*Math.cos(a),ly=C+(R+38)*Math.sin(a);
    html+=`<g class="node" data-i="${i}"><circle cx="${x}" cy="${y}" r="9" fill="#0E0E10" stroke="#34343b" stroke-width="2"/><text x="${lx}" y="${ly+5}" text-anchor="middle" fill="#6b6b73" font-size="15" font-family="Karantina,sans-serif">${String(i+1).padStart(2,'0')}</text></g>`}
  wheel.setAttribute('viewBox','0 0 560 560');wheel.innerHTML=html;
  const arc=$('.arc',wheel),nodes=$$('.node',wheel);let cur=0,timer;
  const set=i=>{cur=i;steps.forEach((s,j)=>s.classList.toggle('on',j===i));nodes.forEach((g,j)=>{const c=g.querySelector('circle');c.setAttribute('fill',j<=i?'#C8102E':'#0E0E10');c.setAttribute('stroke',j<=i?'#E0263F':'#34343b');g.querySelector('text').setAttribute('fill',j===i?'#EDEAE4':'#6b6b73')});
    arc.style.transition='stroke-dasharray .8s cubic-bezier(.16,1,.3,1)';arc.setAttribute('stroke-dasharray',`${(i/(n-1))*100} 100`)};
  const auto=()=>{clearInterval(timer);if(!RM)timer=setInterval(()=>set((cur+1)%n),2200)};
  steps.forEach((s,i)=>{s.addEventListener('mouseenter',()=>{clearInterval(timer);set(i)});s.addEventListener('mouseleave',auto)});
  new IntersectionObserver(([e])=>{if(e.isIntersecting){set(0);auto()}else clearInterval(timer)},{threshold:.3}).observe(wheel);
  set(0);}

/* marquee duplication (keeps HTML lean & crawlable once) */
$$('.track,.qtrack').forEach(t=>{t.innerHTML+=t.innerHTML;[...t.children].slice(t.children.length/2).forEach(c=>c.setAttribute('aria-hidden','true'))});
})();
/* lazy video */
(()=>{const vs=[...document.querySelectorAll('video[data-lazyplay]')];if(!vs.length)return;
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
const io=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){v.play().catch(()=>{})}else v.pause()}),{threshold:.25});vs.forEach(v=>io.observe(v))})();
/* copy bios */
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>{const t=b.parentElement.querySelector('p:last-of-type').innerText;navigator.clipboard&&navigator.clipboard.writeText(t).then(()=>{b.textContent='הועתק ✓';setTimeout(()=>b.textContent='העתקה',1800)})}));
/* lite youtube */
document.querySelectorAll('.yt[data-yt]').forEach(b=>b.addEventListener('click',()=>{const f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0';f.allow='autoplay; encrypted-media; picture-in-picture';f.allowFullscreen=true;f.title='סרטון';b.replaceChildren(f)},{once:true}));
/* drive video lazy player */
document.querySelectorAll('.dv[data-dv]').forEach(b=>b.addEventListener('click',()=>{const f=document.createElement('iframe');f.src='https://drive.google.com/file/d/'+b.dataset.dv+'/preview';f.allow='autoplay; fullscreen';f.allowFullscreen=true;f.title='קורס שפת הגוף';b.replaceChildren(f)},{once:true}));
