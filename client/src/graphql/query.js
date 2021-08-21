export const PHOTO = `
  query myQuery ($id: ID!){
    photo (id: $id){
      id
      width
      height
      faces {
        id
        location
        landmarks {
          chin
          left_eyebrow
          right_eyebrow
          nose_bridge
          nose_tip
          left_eye
          right_eye
          top_lip
          bottom_lip
        }
        encoding
        profile {
          id
          name
        }
      }
    }
  }
`

export const IDENTIFYFACE = `
  query identifyFace($id: String!){
    identifyFace(id: $id) {
      id
      status
      current
      total
      result {
        id
        score
      }
    }
  }
`

export const PROFILE = `
  query profile($id: ID!) {
    profile (id: $id) {
      id
      name
      facesCount
      thumbnail {
        location
        photo {
          id
          width
          height
        }
      }
    }
  }
`