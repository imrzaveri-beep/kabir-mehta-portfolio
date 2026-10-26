import localFont from 'next/font/local';
import {Header,Cursor,Reveal} from '@/components/interactive';
import {Footer} from '@/components/pages';
import {asset,whatsapp,SITE} from '@/lib/data';
import './globals.css';
const inter=localFont({src:'../public/fonts/inter.woff2',variable:'--font-inter',display:'swap',weight:'400 700'});
const space=localFont({src:'../public/fonts/space-grotesk.woff2',variable:'--font-space',display:'swap',weight:'400 700'});
const mono=localFont({src:'../public/fonts/jetbrains-mono.woff2',variable:'--font-mono',display:'swap',weight:'400 700'});
export const metadata={metadataBase:new URL(SITE+'/'),title:{default:'Kabir Mehta | Product Designer',template:'%s | Kabir Mehta'},description:'A fictional product design portfolio exploring fintech, health and commerce.',icons:{icon:asset('favicon.svg')},openGraph:{type:'website',siteName:'Kabir Mehta',images:[SITE+'/images/og-home.png']}};
export default function RootLayout({children}){return <html lang="en" data-theme="dark" suppressHydrationWarning><head><script dangerouslySetInnerHTML={{__html:"try{document.documentElement.dataset.theme=localStorage.getItem('km-theme')==='light'?'light':'dark'}catch(e){}"}}/></head><body className={`${inter.variable} ${space.variable} ${mono.variable}`}><a className="skip-link" href="#main">Skip to content</a><Header/><main id="main" tabIndex={-1}><Reveal>{children}</Reveal></main><Footer/><a className="whatsapp" href={whatsapp()} target="_blank" rel="noreferrer" aria-label="Chat with Kabir on WhatsApp"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 11.7a8 8 0 0 1-11.8 7L4 20l1.3-4.2A8 8 0 1 1 20 11.7Z" stroke="currentColor" strokeWidth="1.5"/><path d="M9 7.5c-2 2 3.5 7.5 5.5 5.5l-1.4-1.2-1 .7-2.6-2.6.7-1L9 7.5Z" fill="currentColor"/></svg><span>Let’s chat</span></a><Cursor/></body></html>}
