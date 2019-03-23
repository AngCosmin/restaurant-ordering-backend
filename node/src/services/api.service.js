import axios from 'axios'

const instance = axios.create({
    baseURL: `http://localhost:5000`,
    headers: {
        'Authorization': {
            toString() {
                return `Bearer 123`
            }
        }
    }
})

export default instance
