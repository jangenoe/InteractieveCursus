var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,o,i,u,l,d,f,s,c,p,b,h,v,y,g,m,j,w={244:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(44),t.e(568)]).then((()=>()=>t(568))),"./extension":()=>Promise.all([t.e(44),t.e(506)]).then((()=>()=>t(506)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a="default",n=t.S[a];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>n,init:()=>o})}},k={};function P(e){var r=k[e];if(void 0!==r)return r.exports;var t=k[e]={id:e,exports:{}};return w[e](t,t.exports,P),t.exports}P.m=w,P.c=k,P.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return P.d(r,{a:r}),r},r=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,P.t=function(t,a){if(1&a&&(t=this(t)),8&a)return t;if("object"==typeof t&&t){if(4&a&&t.__esModule)return t;if(16&a&&"function"==typeof t.then)return t}var n=Object.create(null);P.r(n);var o={};e=e||[null,r({}),r([]),r(r)];for(var i=2&a&&t;"object"==typeof i&&!~e.indexOf(i);i=r(i))Object.getOwnPropertyNames(i).forEach((e=>o[e]=()=>t[e]));return o.default=()=>t,P.d(n,o),n},P.d=(e,r)=>{for(var t in r)P.o(r,t)&&!P.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},P.f={},P.e=e=>Promise.all(Object.keys(P.f).reduce(((r,t)=>(P.f[t](e,r),r)),[])),P.u=e=>e+"."+{44:"39db1483e6068de6cf92",82:"fcc5489b97181d5cdeb5",154:"4a7913c09e75fc60c1f1",176:"14a086d68b2525bcd250",222:"3b93934d4eaeabb96283",506:"f90dc1516f0a4cb868e3",568:"2f814165422050e9df90"}[e]+".js?v="+{44:"39db1483e6068de6cf92",82:"fcc5489b97181d5cdeb5",154:"4a7913c09e75fc60c1f1",176:"14a086d68b2525bcd250",222:"3b93934d4eaeabb96283",506:"f90dc1516f0a4cb868e3",568:"2f814165422050e9df90"}[e],P.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),P.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),t={},a="@deathbeds/jupyterlab-deck:",P.l=(e,r,n,o)=>{if(t[e])t[e].push(r);else{var i,u;if(void 0!==n)for(var l=document.getElementsByTagName("script"),d=0;d<l.length;d++){var f=l[d];if(f.getAttribute("src")==e||f.getAttribute("data-webpack")==a+n){i=f;break}}i||(u=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,P.nc&&i.setAttribute("nonce",P.nc),i.setAttribute("data-webpack",a+n),i.src=e),t[e]=[r];var s=(r,a)=>{i.onerror=i.onload=null,clearTimeout(c);var n=t[e];if(delete t[e],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(a))),r)return r(a)},c=setTimeout(s.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=s.bind(null,i.onerror),i.onload=s.bind(null,i.onload),u&&document.head.appendChild(i)}},P.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{P.S={};var e={},r={};P.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];P.o(P.S,t)||(P.S[t]={});var o=P.S[t],i="@deathbeds/jupyterlab-deck",u=(e,r,t,a)=>{var n=o[e]=o[e]||{},u=n[r];(!u||!u.loaded&&(!a!=!u.eager?a:i>u.from))&&(n[r]={get:t,from:i,eager:!!a})},l=[];return"default"===t&&(u("@deathbeds/jupyterlab-deck","0.2.0",(()=>Promise.all([P.e(44),P.e(568)]).then((()=>()=>P(568))))),u("d3-drag","3.0.0",(()=>Promise.all([P.e(176),P.e(82)]).then((()=>()=>P(82)))))),e[t]=l.length?Promise.all(l).then((()=>e[t]=1)):1}}})(),(()=>{var e;P.g.importScripts&&(e=P.g.location+"");var r=P.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var a=t.length-1;a>-1&&!e;)e=t[a--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),P.p=e})(),n=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},o=(e,r)=>{e=n(e),r=n(r);for(var t=0;;){if(t>=e.length)return t<r.length&&"u"!=(typeof r[t])[0];var a=e[t],o=(typeof a)[0];if(t>=r.length)return"u"==o;var i=r[t],u=(typeof i)[0];if(o!=u)return"o"==o&&"n"==u||"s"==u||"u"==o;if("o"!=o&&"u"!=o&&a!=i)return a<i;t++}},i=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,n=1;n<e.length;n++)a--,t+="u"==(typeof(u=e[n]))[0]?"-":(a>0?".":"")+(a=2,u);return t}var o=[];for(n=1;n<e.length;n++){var u=e[n];o.push(0===u?"not("+l()+")":1===u?"("+l()+" || "+l()+")":2===u?o.pop()+" "+o.pop():i(u))}return l();function l(){return o.pop().replace(/^\((.+)\)$/,"$1")}},u=(e,r)=>{if(0 in e){r=n(r);var t=e[0],a=t<0;a&&(t=-t-1);for(var o=0,i=1,l=!0;;i++,o++){var d,f,s=i<e.length?(typeof e[i])[0]:"";if(o>=r.length||"o"==(f=(typeof(d=r[o]))[0]))return!l||("u"==s?i>t&&!a:""==s!=a);if("u"==f){if(!l||"u"!=s)return!1}else if(l)if(s==f)if(i<=t){if(d!=e[i])return!1}else{if(a?d>e[i]:d<e[i])return!1;d!=e[i]&&(l=!1)}else if("s"!=s&&"n"!=s){if(a||i<=t)return!1;l=!1,i--}else{if(i<=t||f<s!=a)return!1;l=!1}else"s"!=s&&"n"!=s&&(l=!1,i--)}}var c=[],p=c.pop.bind(c);for(o=1;o<e.length;o++){var b=e[o];c.push(1==b?p()|p():2==b?p()&p():b?u(b,r):!p())}return!!p()},l=(e,r)=>{var t=P.S[e];if(!t||!P.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},d=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&o(e,r)?r:e),0)},f=(e,r,t,a)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+i(a)+")",s=(e,r,t,a)=>{var n=d(e,t);return u(a,n)||p(f(e,t,n,a)),b(e[t][n])},c=(e,r,t)=>{var a=e[r];return(r=Object.keys(a).reduce(((e,r)=>!u(t,r)||e&&!o(e,r)?e:r),0))&&a[r]},p=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},b=e=>(e.loaded=1,e.get()),v=(h=e=>function(r,t,a,n){var o=P.I(r);return o&&o.then?o.then(e.bind(e,r,P.S[r],t,a,n)):e(r,P.S[r],t,a,n)})(((e,r,t,a)=>(l(e,t),s(r,0,t,a)))),y=h(((e,r,t,a,n)=>{var o=r&&P.o(r,t)&&c(r,t,a);return o?b(o):n()})),g={},m={85:()=>v("default","@jupyterlab/ui-components",[1,4,0,9]),300:()=>v("default","@deathbeds/jupyterlab-fonts",[1,3,0,0]),930:()=>v("default","@lumino/coreutils",[1,2,0,0]),29:()=>v("default","react",[1,18,2,0]),53:()=>v("default","@jupyterlab/translation",[1,4,0,9]),122:()=>v("default","@jupyterlab/notebook",[1,4,0,9]),165:()=>v("default","@jupyterlab/docmanager",[1,4,0,9]),190:()=>v("default","@jupyterlab/settingregistry",[1,4,0,9]),205:()=>v("default","@jupyterlab/application",[1,4,0,9]),308:()=>v("default","@jupyterlab/apputils",[1,4,1,9]),462:()=>v("default","@jupyterlab/markdownviewer",[1,4,0,9]),593:()=>v("default","@lumino/domutils",[1,2,0,0]),667:()=>v("default","@jupyterlab/statusbar",[1,4,0,9]),697:()=>v("default","@lumino/algorithm",[1,2,0,0]),717:()=>v("default","@lumino/disposable",[1,2,0,0]),749:()=>v("default","@jupyterlab/coreutils",[1,6,0,9]),778:()=>v("default","@lumino/widgets",[1,2,0,1]),901:()=>v("default","@lumino/signaling",[1,2,0,0]),977:()=>v("default","@jupyterlab/fileeditor",[1,4,0,9]),334:()=>y("default","d3-drag",[1,3],(()=>P.e(222).then((()=>()=>P(82)))))},j={44:[85,300,930],154:[334],506:[29,53,122,165,190,205,308,462,593,667,697,717,749,778,901,977]},P.f.consumes=(e,r)=>{P.o(j,e)&&j[e].forEach((e=>{if(P.o(g,e))return r.push(g[e]);var t=r=>{g[e]=0,P.m[e]=t=>{delete P.c[e],t.exports=r()}},a=r=>{delete g[e],P.m[e]=t=>{throw delete P.c[e],r}};try{var n=m[e]();n.then?r.push(g[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{var e={91:0};P.f.j=(r,t)=>{var a=P.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(44!=r){var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var o=P.p+P.u(r),i=new Error;P.l(o,(t=>{if(P.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",i.name="ChunkLoadError",i.type=n,i.request=o,a[1](i)}}),"chunk-"+r,r)}else e[r]=0};var r=(r,t)=>{var a,n,[o,i,u]=t,l=0;if(o.some((r=>0!==e[r]))){for(a in i)P.o(i,a)&&(P.m[a]=i[a]);u&&u(P)}for(r&&r(t);l<o.length;l++)n=o[l],P.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunk_deathbeds_jupyterlab_deck=self.webpackChunk_deathbeds_jupyterlab_deck||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),P.nc=void 0;var _=P(244);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@deathbeds/jupyterlab-deck"]=_})();
//# sourceMappingURL=remoteEntry.009d8686d52fe5d2e0a6.js.map