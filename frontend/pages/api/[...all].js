import getConfig from 'next/config'
import httpProxyMiddleware from 'next-http-proxy-middleware'

const {serverRuntimeConfig} = getConfig()

export const config = {
  api: {
    bodyParser: false,
  },
}

export default function handler(req, res) {
  return httpProxyMiddleware(req, res, {
    target: serverRuntimeConfig.backendUrl,
  })
}
