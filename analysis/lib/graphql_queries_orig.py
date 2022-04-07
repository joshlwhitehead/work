idTokenQuery = """
  query IdToken ($refreshToken: String!) {
    token_from_refresh (refreshToken:$refreshToken) {
      idToken
      expiresIn
    }
  }
"""


consumableWhere = """
query LastConsumableWithResults($where: consumable_bool_exp) {
  consumable (
    limit: 50000
    where: $where
    order_by: [
      {
        updatedAt: desc
      }
    ]
  ){
    id
    manufactureStartTime
    manufactureEndTime
    manufactureVersion
    batch
    consumableSteps {
      id
      step
      process
      value
      person
      startTime
      endTime
      comments
    }
    experiments {
      id
      experimentStartTime
      experimentEndTime
      currentStep
      memo
      hasError
      errors
      protocol {
        id
        name
      }
      instrument {
        id
        name
        location
      }
      experimentResult {
        id
      	pcrData
        meltData
        hasBeenAnalyzed
        pcrResultData
        meltResultData
      }
    }
  }
}
"""

