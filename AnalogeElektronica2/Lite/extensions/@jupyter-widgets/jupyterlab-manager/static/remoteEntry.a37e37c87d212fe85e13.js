var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,o,i,u,l,d,f,s,c,p,b,h,m,g,v,y,j,w,P,S,k={5348:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(869),t.e(67),t.e(930),t.e(388),t.e(134)]).then((()=>()=>t(134))),"./extension":()=>Promise.all([t.e(869),t.e(67),t.e(930),t.e(388),t.e(134)]).then((()=>()=>t(134)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a="default",n=t.S[a];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>n,init:()=>o})}},E={};function _(e){var r=E[e];if(void 0!==r)return r.exports;var t=E[e]={id:e,loaded:!1,exports:{}};return k[e].call(t.exports,t,t.exports,_),t.loaded=!0,t.exports}_.m=k,_.c=E,_.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return _.d(r,{a:r}),r},_.d=(e,r)=>{for(var t in r)_.o(r,t)&&!_.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},_.f={},_.e=e=>Promise.all(Object.keys(_.f).reduce(((r,t)=>(_.f[t](e,r),r)),[])),_.u=e=>(863===e?"@jupyter-widgets/controls":e)+"."+{61:"21f571face17e35076c2",67:"760f0b2ce7647388b914",113:"e4cfda62b59ddbe550d3",134:"a63a8d293fb35a52dc25",291:"cff5ef71b29e18850479",336:"ebc7a55ea1768712771f",345:"17494fea1ff555b26294",388:"7b9bc65ab3b0b744fe93",495:"79062b4ce5ec7920dcb1",595:"74686e2543ce21f10975",596:"df8214a14175baf1ee16",633:"2cbcc5998e25c5521f72",644:"558670f1aa9ae5791769",699:"e966b1425a7d4e8c3f4e",863:"f3d34622f50c9be50b4f",869:"19bd6b2dbf5f1e6c9f81",930:"b32c52301e934bfecc7d",965:"9a2bfc1116cea35345ca"}[e]+".js?v="+{61:"21f571face17e35076c2",67:"760f0b2ce7647388b914",113:"e4cfda62b59ddbe550d3",134:"a63a8d293fb35a52dc25",291:"cff5ef71b29e18850479",336:"ebc7a55ea1768712771f",345:"17494fea1ff555b26294",388:"7b9bc65ab3b0b744fe93",495:"79062b4ce5ec7920dcb1",595:"74686e2543ce21f10975",596:"df8214a14175baf1ee16",633:"2cbcc5998e25c5521f72",644:"558670f1aa9ae5791769",699:"e966b1425a7d4e8c3f4e",863:"f3d34622f50c9be50b4f",869:"19bd6b2dbf5f1e6c9f81",930:"b32c52301e934bfecc7d",965:"9a2bfc1116cea35345ca"}[e],_.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),_.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="@jupyter-widgets/jupyterlab-manager:",_.l=(t,a,n,o)=>{if(e[t])e[t].push(a);else{var i,u;if(void 0!==n)for(var l=document.getElementsByTagName("script"),d=0;d<l.length;d++){var f=l[d];if(f.getAttribute("src")==t||f.getAttribute("data-webpack")==r+n){i=f;break}}i||(u=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,_.nc&&i.setAttribute("nonce",_.nc),i.setAttribute("data-webpack",r+n),i.src=t),e[t]=[a];var s=(r,a)=>{i.onerror=i.onload=null,clearTimeout(c);var n=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(a))),r)return r(a)},c=setTimeout(s.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=s.bind(null,i.onerror),i.onload=s.bind(null,i.onload),u&&document.head.appendChild(i)}},_.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},_.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{_.S={};var e={},r={};_.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];_.o(_.S,t)||(_.S[t]={});var o=_.S[t],i="@jupyter-widgets/jupyterlab-manager",u=(e,r,t,a)=>{var n=o[e]=o[e]||{},u=n[r];(!u||!u.loaded&&(!a!=!u.eager?a:i>u.from))&&(n[r]={get:t,from:i,eager:!!a})},l=[];return"default"===t&&(u("@jupyter-widgets/base-manager","1.0.7",(()=>Promise.all([_.e(113),_.e(869),_.e(930),_.e(336)]).then((()=>()=>_(6110))))),u("@jupyter-widgets/base","6.0.6",(()=>Promise.all([_.e(644),_.e(67),_.e(633),_.e(930),_.e(595)]).then((()=>()=>_(9185))))),u("@jupyter-widgets/controls","5.0.7",(()=>Promise.all([_.e(345),_.e(869),_.e(67),_.e(633),_.e(495),_.e(388),_.e(61)]).then((()=>()=>_(2495))))),u("@jupyter-widgets/jupyterlab-manager","5.0.9",(()=>Promise.all([_.e(869),_.e(67),_.e(930),_.e(388),_.e(134)]).then((()=>()=>_(134))))),u("@jupyter-widgets/output","6.0.6",(()=>Promise.all([_.e(869),_.e(965)]).then((()=>()=>_(2965))))),u("jquery","3.7.0",(()=>_.e(291).then((()=>()=>_(8291))))),u("semver","7.5.1",(()=>_.e(699).then((()=>()=>_(7699)))))),e[t]=l.length?Promise.all(l).then((()=>e[t]=1)):1}}})(),(()=>{var e;_.g.importScripts&&(e=_.g.location+"");var r=_.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var a=t.length-1;a>-1&&!e;)e=t[a--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),_.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],o=(typeof n)[0];if(a>=r.length)return"u"==o;var i=r[a],u=(typeof i)[0];if(o!=u)return"o"==o&&"n"==u||"s"==u||"u"==o;if("o"!=o&&"u"!=o&&n!=i)return n<i;a++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,o=1;o<e.length;o++)a--,t+="u"==(typeof(u=e[o]))[0]?"-":(a>0?".":"")+(a=2,u);return t}var i=[];for(o=1;o<e.length;o++){var u=e[o];i.push(0===u?"not("+l()+")":1===u?"("+l()+" || "+l()+")":2===u?i.pop()+" "+i.pop():n(u))}return l();function l(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var i=0,u=1,l=!0;;u++,i++){var d,f,s=u<e.length?(typeof e[u])[0]:"";if(i>=r.length||"o"==(f=(typeof(d=r[i]))[0]))return!l||("u"==s?u>a&&!n:""==s!=n);if("u"==f){if(!l||"u"!=s)return!1}else if(l)if(s==f)if(u<=a){if(d!=e[u])return!1}else{if(n?d>e[u]:d<e[u])return!1;d!=e[u]&&(l=!1)}else if("s"!=s&&"n"!=s){if(n||u<=a)return!1;l=!1,u--}else{if(u<=a||f<s!=n)return!1;l=!1}else"s"!=s&&"n"!=s&&(l=!1,u--)}}var c=[],p=c.pop.bind(c);for(i=1;i<e.length;i++){var b=e[i];c.push(1==b?p()|p():2==b?p()&p():b?o(b,r):!p())}return!!p()},i=(e,r)=>{var t=_.S[e];if(!t||!_.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},u=(e,r)=>{var t=e[r];return(r=Object.keys(t).reduce(((e,r)=>!e||a(e,r)?r:e),0))&&t[r]},l=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},d=(e,r,t,a)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+n(a)+")",f=(e,r,t,a)=>{var n=l(e,t);return o(a,n)||p(d(e,t,n,a)),h(e[t][n])},s=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!o(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},c=(e,r,t,a)=>{var o=e[t];return"No satisfying version ("+n(a)+") of shared module "+t+" found in shared scope "+r+".\nAvailable versions: "+Object.keys(o).map((e=>e+" from "+o[e].from)).join(", ")},p=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},b=(e,r,t,a)=>{p(c(e,r,t,a))},h=e=>(e.loaded=1,e.get()),g=(m=e=>function(r,t,a,n){var o=_.I(r);return o&&o.then?o.then(e.bind(e,r,_.S[r],t,a,n)):e(r,_.S[r],t,a,n)})(((e,r,t,a)=>r&&_.o(r,t)?h(u(r,t)):a())),v=m(((e,r,t,a)=>(i(e,t),h(s(r,t,a)||b(r,e,t,a)||u(r,t))))),y=m(((e,r,t,a)=>(i(e,t),f(r,0,t,a)))),j=m(((e,r,t,a,n)=>{var o=r&&_.o(r,t)&&s(r,t,a);return o?h(o):n()})),w={},P={4869:()=>j("default","@jupyter-widgets/base",[1,6,0,6],(()=>Promise.all([_.e(644),_.e(67),_.e(633),_.e(930),_.e(595)]).then((()=>()=>_(9185))))),2994:()=>j("default","jquery",[1,3,1,1],(()=>_.e(291).then((()=>()=>_(8291))))),8778:()=>y("default","@lumino/widgets",[1,2,0,1]),7930:()=>y("default","@lumino/coreutils",[1,2,0,0]),4901:()=>y("default","@lumino/signaling",[1,2,0,0]),6697:()=>y("default","@lumino/algorithm",[1,2,0,0]),452:()=>y("default","@jupyterlab/translation",[1,4,0,5]),1426:()=>y("default","@jupyterlab/settingregistry",[1,4,0,5]),2212:()=>y("default","@jupyterlab/notebook",[1,4,0,5]),2380:()=>y("default","@jupyterlab/services",[1,7,0,5]),3004:()=>y("default","@lumino/properties",[1,2,0,0]),4339:()=>v("default","@jupyterlab/outputarea",[1,4,0,5]),5243:()=>y("default","@jupyterlab/logconsole",[1,4,0,5]),7463:()=>y("default","@jupyterlab/rendermime",[1,4,0,5]),7631:()=>j("default","@jupyter-widgets/base-manager",[1,1,0,7],(()=>Promise.all([_.e(113),_.e(336)]).then((()=>()=>_(6110))))),7717:()=>y("default","@lumino/disposable",[1,2,0,0]),8177:()=>j("default","@jupyter-widgets/output",[1,6,0,6],(()=>_.e(596).then((()=>()=>_(2965))))),9e3:()=>j("default","semver",[1,7,3,5],(()=>_.e(699).then((()=>()=>_(7699))))),9450:()=>y("default","@jupyterlab/mainmenu",[1,4,0,5]),5633:()=>y("default","@lumino/messaging",[1,2,0,0]),8830:()=>g("default","jquery",(()=>_.e(291).then((()=>()=>_(8291))))),5593:()=>y("default","@lumino/domutils",[1,2,0,0]),342:()=>j("default","@jupyter-widgets/controls",[1,5,0,7],(()=>Promise.all([_.e(345),_.e(633),_.e(495)]).then((()=>()=>_(2495)))))},S={67:[2994,8778],134:[452,1426,2212,2380,3004,4339,5243,7463,7631,7717,8177,9e3,9450],388:[4901,6697],495:[5593],595:[8830],633:[5633],863:[342],869:[4869],930:[7930]},_.f.consumes=(e,r)=>{_.o(S,e)&&S[e].forEach((e=>{if(_.o(w,e))return r.push(w[e]);var t=r=>{w[e]=0,_.m[e]=t=>{delete _.c[e],t.exports=r()}},a=r=>{delete w[e],_.m[e]=t=>{throw delete _.c[e],r}};try{var n=P[e]();n.then?r.push(w[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{_.b=document.baseURI||self.location.href;var e={513:0};_.f.j=(r,t)=>{var a=_.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(/^(86[39]|388|633|67|930)$/.test(r))e[r]=0;else{var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var o=_.p+_.u(r),i=new Error;_.l(o,(t=>{if(_.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",i.name="ChunkLoadError",i.type=n,i.request=o,a[1](i)}}),"chunk-"+r,r)}};var r=(r,t)=>{var a,n,[o,i,u]=t,l=0;if(o.some((r=>0!==e[r]))){for(a in i)_.o(i,a)&&(_.m[a]=i[a]);u&&u(_)}for(r&&r(t);l<o.length;l++)n=o[l],_.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunk_jupyter_widgets_jupyterlab_manager=self.webpackChunk_jupyter_widgets_jupyterlab_manager||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),_.nc=void 0;var x=_(5348);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@jupyter-widgets/jupyterlab-manager"]=x})();