#include "commons.h"
#include "finance-proto-models/build/cpp/envelope.pb.h"
#include <gtest/gtest.h>

TEST(CommonsTest, Add) {
  FinanceProtobufModels::PriceAggregationEnvelope envelope;
  envelope.set_provider(FinanceProtobufModels::Provider::COINBASE);
  EXPECT_EQ(Commons::add(1, 2), 3);
}