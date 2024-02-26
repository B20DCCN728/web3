import json

from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Infura API key and Ethereum address
# Fill in your Infura URL and Ethereum wallet private key
infura_url = ""
wallet_private_key = ""

# Check if environment variables are set
if infura_url is None or wallet_private_key is None:
    raise ValueError("INFURA_URL or WALLET_PRIVATE_KEY environment variable not set")

# Contract ABI
contract_abi = [
    {
        "inputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [

        ],
        "name": "CreatorPayoutAddressCannotBeZeroAddress",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "DuplicateFeeRecipient",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "DuplicatePayer",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "FeeRecipientCannotBeZeroAddress",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "FeeRecipientNotAllowed",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "FeeRecipientNotPresent",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "want",
                "type": "uint256"
            }
        ],
        "name": "IncorrectPayment",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "feeBps",
                "type": "uint256"
            }
        ],
        "name": "InvalidFeeBps",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidProof",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recoveredSigner",
                "type": "address"
            }
        ],
        "name": "InvalidSignature",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maximum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedEndTime",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minimumOrMaximum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedFeeBps",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maximum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedMaxTokenSupplyForStage",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maximum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedMaxTotalMintableByWallet",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minimum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedMintPrice",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "got",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minimum",
                "type": "uint256"
            }
        ],
        "name": "InvalidSignedStartTime",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "MintQuantityCannotBeZero",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "allowed",
                "type": "uint256"
            }
        ],
        "name": "MintQuantityExceedsMaxMintedPerWallet",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxSupply",
                "type": "uint256"
            }
        ],
        "name": "MintQuantityExceedsMaxSupply",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxTokenSupplyForStage",
                "type": "uint256"
            }
        ],
        "name": "MintQuantityExceedsMaxTokenSupplyForStage",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "currentTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "startTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "endTimestamp",
                "type": "uint256"
            }
        ],
        "name": "NotActive",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "OnlyINonFungibleSeaDropToken",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "PayerCannotBeZeroAddress",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "PayerNotAllowed",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "PayerNotPresent",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "SignatureAlreadyUsed",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "SignedMintsMustRestrictFeeRecipients",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "SignerCannotBeZeroAddress",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "SignerNotPresent",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "TokenGatedDropAllowedNftTokenCannotBeDropToken",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "TokenGatedDropAllowedNftTokenCannotBeZeroAddress",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "TokenGatedDropStageNotPresent",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "allowedNftTokenId",
                "type": "uint256"
            }
        ],
        "name": "TokenGatedNotTokenOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "allowedNftTokenId",
                "type": "uint256"
            }
        ],
        "name": "TokenGatedTokenIdAlreadyRedeemed",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "previousMerkleRoot",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "newMerkleRoot",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "string[]",
                "name": "publicKeyURI",
                "type": "string[]"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "allowListURI",
                "type": "string"
            }
        ],
        "name": "AllowListUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "AllowedFeeRecipientUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newPayoutAddress",
                "type": "address"
            }
        ],
        "name": "CreatorPayoutAddressUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "newDropURI",
                "type": "string"
            }
        ],
        "name": "DropURIUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "payer",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "PayerUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "indexed": False,
                "internalType": "struct PublicDrop",
                "name": "publicDrop",
                "type": "tuple"
            }
        ],
        "name": "PublicDropUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "minter",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "payer",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "quantityMinted",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "unitMintPrice",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "feeBps",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "dropStageIndex",
                "type": "uint256"
            }
        ],
        "name": "SeaDropMint",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "signer",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "minMintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint24",
                        "name": "maxMaxTotalMintableByWallet",
                        "type": "uint24"
                    },
                    {
                        "internalType": "uint40",
                        "name": "minStartTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxEndTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxMaxTokenSupplyForStage",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint16",
                        "name": "minFeeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxFeeBps",
                        "type": "uint16"
                    }
                ],
                "indexed": False,
                "internalType": "struct SignedMintValidationParams",
                "name": "signedMintValidationParams",
                "type": "tuple"
            }
        ],
        "name": "SignedMintValidationParamsUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint8",
                        "name": "dropStageIndex",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxTokenSupplyForStage",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "indexed": False,
                "internalType": "struct TokenGatedDropStage",
                "name": "dropStage",
                "type": "tuple"
            }
        ],
        "name": "TokenGatedDropStageUpdated",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getAllowListMerkleRoot",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getAllowedFeeRecipients",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "allowedNftTokenId",
                "type": "uint256"
            }
        ],
        "name": "getAllowedNftTokenIdIsRedeemed",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getCreatorPayoutAddress",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            }
        ],
        "name": "getFeeRecipientIsAllowed",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "payer",
                "type": "address"
            }
        ],
        "name": "getPayerIsAllowed",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getPayers",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getPublicDrop",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct PublicDrop",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "signer",
                "type": "address"
            }
        ],
        "name": "getSignedMintValidationParams",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "minMintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint24",
                        "name": "maxMaxTotalMintableByWallet",
                        "type": "uint24"
                    },
                    {
                        "internalType": "uint40",
                        "name": "minStartTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxEndTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxMaxTokenSupplyForStage",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint16",
                        "name": "minFeeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxFeeBps",
                        "type": "uint16"
                    }
                ],
                "internalType": "struct SignedMintValidationParams",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getSigners",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            }
        ],
        "name": "getTokenGatedAllowedTokens",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            }
        ],
        "name": "getTokenGatedDrop",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint8",
                        "name": "dropStageIndex",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxTokenSupplyForStage",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct TokenGatedDropStage",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "minterIfNotPayer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "mintPrice",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "startTime",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "endTime",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "dropStageIndex",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxTokenSupplyForStage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "feeBps",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct MintParams",
                "name": "mintParams",
                "type": "tuple"
            },
            {
                "internalType": "bytes32[]",
                "name": "proof",
                "type": "bytes32[]"
            }
        ],
        "name": "mintAllowList",
        "outputs": [

        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "minterIfNotPayer",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "allowedNftToken",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "allowedNftTokenIds",
                        "type": "uint256[]"
                    }
                ],
                "internalType": "struct TokenGatedMintParams",
                "name": "mintParams",
                "type": "tuple"
            }
        ],
        "name": "mintAllowedTokenHolder",
        "outputs": [

        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "minterIfNotPayer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            }
        ],
        "name": "mintPublic",
        "outputs": [

        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftContract",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "minterIfNotPayer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "mintPrice",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "startTime",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "endTime",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "dropStageIndex",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxTokenSupplyForStage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "feeBps",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct MintParams",
                "name": "mintParams",
                "type": "tuple"
            },
            {
                "internalType": "uint256",
                "name": "salt",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "signature",
                "type": "bytes"
            }
        ],
        "name": "mintSigned",
        "outputs": [

        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "bytes32",
                        "name": "merkleRoot",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "string[]",
                        "name": "publicKeyURIs",
                        "type": "string[]"
                    },
                    {
                        "internalType": "string",
                        "name": "allowListURI",
                        "type": "string"
                    }
                ],
                "internalType": "struct AllowListData",
                "name": "allowListData",
                "type": "tuple"
            }
        ],
        "name": "updateAllowList",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "updateAllowedFeeRecipient",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_payoutAddress",
                "type": "address"
            }
        ],
        "name": "updateCreatorPayoutAddress",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "dropURI",
                "type": "string"
            }
        ],
        "name": "updateDropURI",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "payer",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "updatePayer",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct PublicDrop",
                "name": "publicDrop",
                "type": "tuple"
            }
        ],
        "name": "updatePublicDrop",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "signer",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "minMintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint24",
                        "name": "maxMaxTotalMintableByWallet",
                        "type": "uint24"
                    },
                    {
                        "internalType": "uint40",
                        "name": "minStartTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxEndTime",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint40",
                        "name": "maxMaxTokenSupplyForStage",
                        "type": "uint40"
                    },
                    {
                        "internalType": "uint16",
                        "name": "minFeeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxFeeBps",
                        "type": "uint16"
                    }
                ],
                "internalType": "struct SignedMintValidationParams",
                "name": "signedMintValidationParams",
                "type": "tuple"
            }
        ],
        "name": "updateSignedMintValidationParams",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "allowedNftToken",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint80",
                        "name": "mintPrice",
                        "type": "uint80"
                    },
                    {
                        "internalType": "uint16",
                        "name": "maxTotalMintableByWallet",
                        "type": "uint16"
                    },
                    {
                        "internalType": "uint48",
                        "name": "startTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint48",
                        "name": "endTime",
                        "type": "uint48"
                    },
                    {
                        "internalType": "uint8",
                        "name": "dropStageIndex",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxTokenSupplyForStage",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint16",
                        "name": "feeBps",
                        "type": "uint16"
                    },
                    {
                        "internalType": "bool",
                        "name": "restrictFeeRecipients",
                        "type": "bool"
                    }
                ],
                "internalType": "struct TokenGatedDropStage",
                "name": "dropStage",
                "type": "tuple"
            }
        ],
        "name": "updateTokenGatedDrop",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract_address = "0x00005EA00Ac477B1030CE78506496e8C2dE24bf5"

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load Ethereum account
account = web3.eth.account.from_key(wallet_private_key)

# Set the default account
web3.eth.default_account = account.address

# Contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def mint_nft(nftContract, feeRecipient, minterIfNotPayer, quantity):
    # Estimate gas for the transaction
    gas_estimate = contract.functions.mintPublic(nftContract, feeRecipient, minterIfNotPayer, quantity).estimate_gas({
        'from': account.address,
    })

    # Encode function call for safeMint
    txn = contract.functions.mintPublic(nftContract, feeRecipient, minterIfNotPayer, quantity).build_transaction({
        'chainId': 80001,
        'gas': gas_estimate,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(account.address),
    })

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=account._private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Wait for the transaction to be mined
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt


# Example usage
nftContract = "0x9d88d7Bb0F5329A59bbDD54159A2B046c0c788B3"
feeRecipient = "0x0000a26b00c1F0DF003000390027140000fAa719"
minterIfNotPayer = "0x0000000000000000000000000000000000000000"
quantity = 100

receipt = mint_nft(nftContract, feeRecipient, minterIfNotPayer, quantity)
print(json.dumps(receipt, indent=4))
