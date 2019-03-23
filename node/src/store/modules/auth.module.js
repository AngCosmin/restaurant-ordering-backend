import axios from '@/services/api.service'
import router from '@/router'

const state = {
	email: null,
	password: null,
}

const mutations = {
	authUser(state, userData) {
		state.email = userData.email
		state.password = userData.password
	},
	clearAuthData(state) {
		state.email = null
		state.password = null
	}

};

const getters = {
	isAuthenticated(state) {
		return state.email !== null
	},
}


const actions = {
	login: ({ commit }, authData) => {
		console.log("1")
		axios.post('/restaurant/login', {
			email: authData.email,
			password: authData.password,
		}).then(response => {
			commit('authUser', { email: authData.email, password: authData.password });
			localStorage.setItem('email', authData.email)
			localStorage.setItem('password', authData.password)
			router.replace('/products');
		}).catch(error => {
			console.error(error);
		})
	},
	autoLogin({ commit, dispatch }) {
		let email = localStorage.getItem('email')
		let password = localStorage.getItem('password')

		if (!email) {
			dispatch('logout')
			return
		}

		commit('authUser', { email: email })
	},
	logout: ({ commit }) => {
		commit('clearAuthData');
		localStorage.removeItem('email');
		localStorage.removeItem('password');
		router.push('/login')
	},
}


export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions,
};

