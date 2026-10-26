import {Home} from '@/components/pages';import {meta,SITE} from '@/lib/data';
export const metadata={title:meta.home[0],description:meta.home[1],alternates:{canonical:SITE+'/'},openGraph:{title:meta.home[0]+' | Kabir Mehta',description:meta.home[1],url:SITE+'/',images:[SITE+'/images/og-home.png']}};
export default function Page(){return <Home/>}
