"use strict";(self.webpackChunkjupyterlab_myst=self.webpackChunkjupyterlab_myst||[]).push([[6838],{74712:n=>{var t=Object.prototype.hasOwnProperty,e=Object.prototype.toString,r=Object.defineProperty,o=Object.getOwnPropertyDescriptor,i=function(n){return"function"==typeof Array.isArray?Array.isArray(n):"[object Array]"===e.call(n)},u=function(n){if(!n||"[object Object]"!==e.call(n))return!1;var r,o=t.call(n,"constructor"),i=n.constructor&&n.constructor.prototype&&t.call(n.constructor.prototype,"isPrototypeOf");if(n.constructor&&!o&&!i)return!1;for(r in n);return void 0===r||t.call(n,r)},c=function(n,t){r&&"__proto__"===t.name?r(n,t.name,{enumerable:!0,configurable:!0,value:t.newValue,writable:!0}):n[t.name]=t.newValue},f=function(n,e){if("__proto__"===e){if(!t.call(n,e))return;if(o)return o(n,e).value}return n[e]};n.exports=function n(){var t,e,r,o,s,l,p=arguments[0],a=1,y=arguments.length,w=!1;for("boolean"==typeof p&&(w=p,p=arguments[1]||{},a=2),(null==p||"object"!=typeof p&&"function"!=typeof p)&&(p={});a<y;++a)if(null!=(t=arguments[a]))for(e in t)r=f(p,e),p!==(o=f(t,e))&&(w&&o&&(u(o)||(s=i(o)))?(s?(s=!1,l=r&&i(r)?r:[]):l=r&&u(r)?r:{},c(p,{name:e,newValue:n(w,l,o)})):void 0!==o&&c(p,{name:e,newValue:o}));return p}},46838:(n,t,e)=>{function r(n){if(n)throw n}e.d(t,{C:()=>l});var o=e(96792),i=e.n(o),u=e(74712),c=e.n(u);function f(n){if("object"!=typeof n||null===n)return!1;const t=Object.getPrototypeOf(n);return!(null!==t&&t!==Object.prototype&&null!==Object.getPrototypeOf(t)||Symbol.toStringTag in n||Symbol.iterator in n)}var s=e(65260);const l=function n(){const t=function(){const n=[],t={run:function(...t){let e=-1;const r=t.pop();if("function"!=typeof r)throw new TypeError("Expected function as last argument, not "+r);!function o(i,...u){const c=n[++e];let f=-1;if(i)r(i);else{for(;++f<t.length;)null!==u[f]&&void 0!==u[f]||(u[f]=t[f]);t=u,c?function(n,t){let e;return function(...t){const i=n.length>t.length;let u;i&&t.push(r);try{u=n.apply(this,t)}catch(n){if(i&&e)throw n;return r(n)}i||(u&&u.then&&"function"==typeof u.then?u.then(o,r):u instanceof Error?r(u):o(u))};function r(n,...r){e||(e=!0,t(n,...r))}function o(n){r(null,n)}}(c,o)(...u):r(null,...u)}}(null,...t)},use:function(e){if("function"!=typeof e)throw new TypeError("Expected `middelware` to be a function, not "+e);return n.push(e),t}};return t}(),e=[];let o,u={},s=-1;return l.data=function(n,t){return"string"==typeof n?2===arguments.length?(h("data",o),u[n]=t,l):p.call(u,n)&&u[n]||null:n?(h("data",o),u=n,l):u},l.Parser=void 0,l.Compiler=void 0,l.freeze=function(){if(o)return l;for(;++s<e.length;){const[n,...r]=e[s];if(!1===r[0])continue;!0===r[0]&&(r[0]=void 0);const o=n.call(l,...r);"function"==typeof o&&t.use(o)}return o=!0,s=Number.POSITIVE_INFINITY,l},l.attachers=e,l.use=function(n,...t){let r;if(h("use",o),null==n);else if("function"==typeof n)a(n,...t);else{if("object"!=typeof n)throw new TypeError("Expected usable value, not `"+n+"`");Array.isArray(n)?p(n):s(n)}return r&&(u.settings=Object.assign(u.settings||{},r)),l;function i(n){if("function"==typeof n)a(n);else{if("object"!=typeof n)throw new TypeError("Expected usable value, not `"+n+"`");if(Array.isArray(n)){const[t,...e]=n;a(t,...e)}else s(n)}}function s(n){p(n.plugins),n.settings&&(r=Object.assign(r||{},n.settings))}function p(n){let t=-1;if(null==n);else{if(!Array.isArray(n))throw new TypeError("Expected a list of plugins, not `"+n+"`");for(;++t<n.length;)i(n[t])}}function a(n,t){let r,o=-1;for(;++o<e.length;)if(e[o][0]===n){r=e[o];break}r?(f(r[1])&&f(t)&&(t=c()(!0,r[1],t)),r[1]=t):e.push([...arguments])}},l.parse=function(n){l.freeze();const t=d(n),e=l.Parser;return y("parse",e),a(e,"parse")?new e(String(t),t).parse():e(String(t),t)},l.stringify=function(n,t){l.freeze();const e=d(t),r=l.Compiler;return w("stringify",r),g(n),a(r,"compile")?new r(n,e).compile():r(n,e)},l.run=function(n,e,r){if(g(n),l.freeze(),r||"function"!=typeof e||(r=e,e=void 0),!r)return new Promise(o);function o(o,i){t.run(n,d(e),(function(t,e,u){e=e||n,t?i(t):o?o(e):r(null,e,u)}))}o(null,r)},l.runSync=function(n,t){let e,o;return l.run(n,t,(function(n,t){r(n),e=t,o=!0})),b("runSync","run",o),e},l.process=function(n,t){if(l.freeze(),y("process",l.Parser),w("process",l.Compiler),!t)return new Promise(e);function e(e,r){const o=d(n);function u(n,o){n||!o?r(n):e?e(o):t(null,o)}l.run(l.parse(o),o,((n,t,e)=>{if(!n&&t&&e){const o=l.stringify(t,e);null==o||("string"==typeof(r=o)||i()(r)?e.value=o:e.result=o),u(n,e)}else u(n);var r}))}e(null,t)},l.processSync=function(n){let t;l.freeze(),y("processSync",l.Parser),w("processSync",l.Compiler);const e=d(n);return l.process(e,(function(n){t=!0,r(n)})),b("processSync","process",t),e},l;function l(){const t=n();let r=-1;for(;++r<e.length;)t.use(...e[r]);return t.data(c()(!0,{},u)),t}}().freeze(),p={}.hasOwnProperty;function a(n,t){return"function"==typeof n&&n.prototype&&(function(n){let t;for(t in n)if(p.call(n,t))return!0;return!1}(n.prototype)||t in n.prototype)}function y(n,t){if("function"!=typeof t)throw new TypeError("Cannot `"+n+"` without `Parser`")}function w(n,t){if("function"!=typeof t)throw new TypeError("Cannot `"+n+"` without `Compiler`")}function h(n,t){if(t)throw new Error("Cannot call `"+n+"` on a frozen processor.\nCreate a new processor first, by calling it: use `processor()` instead of `processor`.")}function g(n){if(!f(n)||"string"!=typeof n.type)throw new TypeError("Expected node, got `"+n+"`")}function b(n,t,e){if(!e)throw new Error("`"+n+"` finished async. Use `"+t+"` instead")}function d(n){return function(n){return Boolean(n&&"object"==typeof n&&"message"in n&&"messages"in n)}(n)?n:new s.I(n)}}}]);